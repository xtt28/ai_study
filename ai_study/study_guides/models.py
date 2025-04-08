from django.contrib.auth import get_user_model
from django.db import models
from django.dispatch import receiver
from .file_parser import parse_pdf
from .tasks import create_outline

class StudyGuide(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="study_guides")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="source_files")
    file_text_data = models.TextField(blank=True)

    def __str__(self):
        return f'Study guide "{self.title}" by {self.user.username}'
    

@receiver(models.signals.post_save, sender=StudyGuide)
def study_guide_after_save(sender, instance, created, *args, **kwargs):
    if created:
        print(f"Study guide {instance} created - parsing PDF.")
        parse_pdf(instance)
        print(f"Generating outline for study guide {instance}")
        create_outline.delay(instance.id)
    
class TextStudyGuide(models.Model):
    study_guide = models.OneToOneField(StudyGuide, on_delete=models.CASCADE, related_name="text_study_guide")
    content = models.TextField()

    def __str__(self):
        return f'Study outline for study guide {self.study_guide}'