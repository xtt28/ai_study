from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from . import models

class StudyGuideDetailView(DetailView):
    model = models.StudyGuide

class StudyGuideCreateView(CreateView):
    model = models.StudyGuide
    fields = ["title", "file"]
    template_name_suffix = "_create"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)