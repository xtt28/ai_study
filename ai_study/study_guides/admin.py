from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(StudyGuide)
admin.site.register(TextStudyGuide)
admin.site.register(FlashCardSet)
admin.site.register(MultipleChoiceTest)