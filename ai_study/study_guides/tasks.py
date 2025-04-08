from celery import shared_task
import importlib

@shared_task
def create_outline(study_guide_id):
    print("hi there guys")
    models = importlib.import_module(".models", "study_guides")
    study_guide = models.StudyGuide.objects.get(id=study_guide_id)
    print(study_guide)
    ai_generate = importlib.import_module(".ai_generate", "study_guides")
    ai_generate.generate_outline(study_guide)