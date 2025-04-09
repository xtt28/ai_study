from django.shortcuts import render
from django.views.generic.detail import DetailView
from . import models

class StudyGuideDetailView(DetailView):
    model = models.StudyGuide
    