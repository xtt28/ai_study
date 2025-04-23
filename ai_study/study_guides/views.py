from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
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
    

class StudyGuideListView(ListView):
    model = models.StudyGuide
    paginate_by = 10
    ordering = "-updated_at"


class StudyGuideUpdateView(UpdateView):
    model = models.StudyGuide
    fields = ["title"]
    template_name_suffix = "_update"

class StudyGuideDeleteView(DeleteView):
    model = models.StudyGuide
    template_name_suffix = "_delete"
