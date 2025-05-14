from celery import shared_task
import importlib

@shared_task
def create_outline(study_guide_id):
    # dynamically import to avoid circular import issues
    models = importlib.import_module(".models", "study_guides")
    study_guide = models.StudyGuide.objects.get(id=study_guide_id)
    ai_generate = importlib.import_module(".ai_generate", "study_guides")
    ai_generate.generate_outline(study_guide)


@shared_task
def create_flashcards(study_guide_id):
    # dynamically import to avoid circular import issues
    models = importlib.import_module(".models", "study_guides")
    study_guide = models.StudyGuide.objects.get(id=study_guide_id)
    ai_generate = importlib.import_module(".ai_generate", "study_guides")
    ai_generate.generate_flashcards(study_guide)