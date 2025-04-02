from django.contrib.auth import get_user_model
from django.db import models

class StudyGuide(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="study_guides")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="source_files")

    def __str__(self):
        return f'Study guide "{self.title}" by {self.user.username}'
    
class TextStudyGuide(models.Model):
    study_guide = models.OneToOneField(StudyGuide, on_delete=models.CASCADE, related_name="text_study_guide")
    content = models.TextField()