from django.conf import settings
from openai import OpenAI
from pydantic import BaseModel
from .models import FlashCardSet, TextStudyGuide

client = OpenAI(api_key=settings.OPENAI_API_KEY)

class FlashCardJsonSchema(BaseModel):
    front: str
    back: str


class FlashCardListJsonSchema(BaseModel):
    cards: list[FlashCardJsonSchema]


class MultipleChoiceQuestionJsonSchema(BaseModel):
    prompt: str
    options: list[str]
    correct_option: str


class MultipleChoiceTestJsonSchema(BaseModel):
    questions: list[MultipleChoiceQuestionJsonSchema]


def generate_outline(study_guide):
    system_prompt = """Use the following transcript extracted from a document to generate a study guide in bullet point outline format, structured with Markdown formatting and headings/subheadings. The study guide should describe the most important content in the transcript. When adding sublevels to a Markdown list, you must indent each sublevel by 4 additional spaces."""
    raw_text = study_guide.file_text_data

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
        {
            "role": "developer",
            "content": system_prompt,
        },
        
        {
            "role": "user",
            "content": raw_text
        }]
    )

    TextStudyGuide.objects.create(study_guide=study_guide, content=response.choices[0].message.content)

def generate_flashcards(study_guide):
    system_prompt = """Use the following transcript extracted from a document to generate a flash card set that covers the most important points of the transcript. The front should have a term in plain text, and the back should have a definition/explanation also in plain text."""
    raw_text = study_guide.file_text_data

    response = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
        {
            "role": "developer",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": raw_text
        }],
        response_format=FlashCardListJsonSchema
    )

    FlashCardSet.objects.create(study_guide=study_guide, data=response.choices[0].message.parsed.dict())