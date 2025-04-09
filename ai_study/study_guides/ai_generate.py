from openai import OpenAI
from django.conf import settings
from .models import TextStudyGuide

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_outline(study_guide):
    system_prompt = """Use the following transcript extracted from a document to generate a study guide in bullet point outline format. Do not add a title or any extra text other than the study guide. When using sublevels in lists, you should indent the sublevels by 4 spaces."""
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
