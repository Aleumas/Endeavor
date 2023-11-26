from langchain.prompts import PromptTemplate
from langchain.chat_models.openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser

from fastapi import FastAPI
from pydantic import BaseModel, Field
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware

from typing import List

llm = ChatOpenAI()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionFeedback(BaseModel):
    """A class that acts as a wrapper for feedback on an individual question response.""" 
    question: str = Field(description="The question for which feedback is provided")
    feedback: str = Field(description="Detailed feedback on the response to the question")
    response: str = Field(description="The user's response to the question") 

class Feedback(BaseModel):
    """A class that acts as a wrapper for feedback on a set of questions."""
    value: QuestionFeedback = Field(description="Feedback on a specific question")
    rating: int = Field(0, description="A rating representing the level of mastery")

@app.get("/feedback/{question}/{response}")
def generate_feedback_for_response(question: str, response: str) -> Feedback:
    """A function that uses LLM to generate feedback for a single question response."""
    parser = PydanticOutputParser(pydantic_object=Feedback)
    format_instructions = parser.get_format_instructions()
    template_text = """generate feedback on the following response: \n
                    '''{response}'''\n
                    to the following question:
                    '''{question}'''
                    Ensure that the feedback is formative in nature, focusing on guiding improvement rather 
                    than just providing a score. Point out specific strengths and areas for growth. Use encouraging language.
                    Additionally, generate a rating on how much the response showed mastery (use a scale from 1-5, 5 being moderate mastery).
                    .\n\n{format_instructions}"""
    prompt_template = PromptTemplate(
        template=template_text,
        input_variables=["question", "response"],
        partial_variables={"format_instructions": format_instructions}
    )

    chain = prompt_template | llm | parser
    return chain.invoke({"question": question, "response": response})

@app.get("/curve-ball/{concept}/{questions}")
def generate_curve_ball_with_questions(concept: str, questions: str) -> str:
    """A function that uses LLM to generate a curve ball question from a list of user defined questions"""
    template_text = """Generate a curveball question on {concept} which is slightly more challenging than the provided list: "{questions}".
                        Ensure that the question is not a compound question. 
                        The question is an addition to the provided list.
                    """

    prompt_template = PromptTemplate(
        template=template_text,
        input_variables=["concept", "questions"],
    )

    chain = prompt_template | llm
    return chain.invoke({"concept": concept, "questions": questions}).content

@app.get("/suggestion/{concept}/{questions}")
def generate_suggestion_with_questions(concept: str, questions: str) -> str:
    """A function that uses LLM to suggests a question from a list of user defined questions"""
    template_text = """Generate a new question on "{concept}" which is of the same difficulty from the provided list: "{questions}". 
                        Ensure that the question is not a compound question. 
                        The question is an addition to the provided list.
                    """

    prompt_template = PromptTemplate(
        template=template_text,
        input_variables=["concept", "questions"],
    )

    chain = prompt_template | llm
    return chain.invoke({"concept": concept, "questions": questions}).content