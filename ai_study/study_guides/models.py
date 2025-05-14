from django.contrib.auth import get_user_model
from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from .file_parser import parse_pdf
from .tasks import create_outline, create_flashcards

class StudyGuide(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="study_guides")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="source_files")
    file_text_data = models.TextField(blank=True)

    def __str__(self):
        return f'Study guide "{self.title}" by {self.user.username}'
    
    def get_absolute_url(self):
        return reverse("study_guides:detail", kwargs={"pk": self.pk})
    

@receiver(models.signals.post_save, sender=StudyGuide)
def study_guide_after_save(sender, instance, created, *args, **kwargs):
    if created:
        print(f"Study guide {instance} created - parsing PDF.")
        parse_pdf(instance)
        print(f"Generating outline for study guide {instance}")
        create_outline.delay(instance.id)
        print(f"Generating flash cards for study guide {instance}")
        create_flashcards.delay(instance.id)
    
class TextStudyGuide(models.Model):
    study_guide = models.OneToOneField(StudyGuide, on_delete=models.CASCADE, related_name="outline")
    content = models.TextField()

    def __str__(self):
        return f'Study outline for {self.study_guide}'
    

class FlashCardSet(models.Model):
    study_guide = models.OneToOneField(StudyGuide, on_delete=models.CASCADE, related_name="flashcards")
    data = models.JSONField()

    def __str__(self):
        return f"Flash cards for {self.study_guide}"
    