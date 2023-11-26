from langchain.prompts import PromptTemplate
from langchain.chat_models.openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser

from fastapi import FastAPI
from pydantic import BaseModel, Field
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware

llm = ChatOpenAI()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Concepts(BaseModel):
    """A class that acts as a wrapper for concept response from LLM."""
    value: list[str] = Field(description="The list of key concepts")

class QuestionFeedback(BaseModel):
   """A class that acts as a wrapper for question feedback from LLM.""" 
   question: str = Field(description="The question whos response is being given feedback on")
   feedback: str = Field(description="The feedback for the response")

class Feedback(BaseModel):
    """A class that acts as a wrapper for question feedback from LLM."""
    value: list[QuestionFeedback] = Field(description="The list of feedback"),
    rating: int = Field(description="The rating for user response"),

@app.get("/feedback/{questions}/{responses}")
def generate_feedback_for_responses(questions: list[str], responses: list[str]) -> Feedback:
    """A function that uses LLM to generate feedback for question responses."""
    parser = PydanticOutputParser(pydantic_object=Feedback)
    format_instructions = parser.get_format_instructions()
    template_text = """generate feedback on the following responses: \n
                    '''{response}'''\n
                    to the following questions:
                    '''{questions}'''
                    Ensure that the feedback is formative in nature, focusing on guiding improvement rather 
                    than just providing a score. Point out specific strengths and areas for growth. For example, 
                    instead of saying, "Incorrect answer," you might say, 
                    "You correctly identified X, but consider exploring Y in more detail." Additionally, generate a rating on how much the response showed mastery (use a scale from 1-5, 5 being moderate mastery).
                    to enhance effective learning for students.\n\n{format_instructions}"""
    prompt_template = PromptTemplate(
        template=template_text,
        input_variables=["questions", "responses"],
        partial_variables={"format_instructions": format_instructions}
    )

    chain = prompt_template | llm | parser
    return chain.invoke({"questions": questions, "responses": responses})

@app.get("/feedback/{subject}/{question}/{response}")
def generate_feedback_for_response(concept: str, question: str, response: str) -> str:
    """A function that uses LLM to generate feedback for a given responce to a question"""
    template_text = """Provide constructive feedback for the question: "{question}" and 
                    the corresponding response: "{response}". Offer guidance on how a 
                    learner can enhance their understanding of the {concept} concept."""

    prompt_template = PromptTemplate(
        template=template_text,
        input_variables=["concept", "question", "response"],
    )

    chain = prompt_template | llm
    return chain.invoke({"concept": concept, "question": question, "response": response}).content

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