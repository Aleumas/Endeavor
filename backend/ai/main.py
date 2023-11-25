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

@app.get("/concepts/{subject}")
def generate_key_concepts_for_subject(subject: str) -> Concepts:
    """A function that uses LLM to generate a list of key concepts for a given subject."""
    parser = PydanticOutputParser(pydantic_object=Concepts)
    format_instructions = parser.get_format_instructions()
    template_text = """Compile a list of (at most) 3 essential concepts related to {subject} 
                    to enhance effective learning for students.\n\n{format_instructions}"""
    prompt_template = PromptTemplate(
        template=template_text,
        input_variables=["subject"],
        partial_variables={"format_instructions": format_instructions}
    )

    chain = prompt_template | llm | parser
    return chain.invoke({"subject": subject})

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