from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from . import models

class StudyGuideDetailView(LoginRequiredMixin, DetailView):
    model = models.StudyGuide

    def get_queryset(self):
        return super().get_queryset().filter(user__id=self.request.user.id)

class StudyGuideCreateView(LoginRequiredMixin, CreateView):
    model = models.StudyGuide
    fields = ["title", "file"]
    template_name_suffix = "_create"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class StudyGuideListView(LoginRequiredMixin, ListView):
    model = models.StudyGuide
    paginate_by = 10
    ordering = "-updated_at"

    def get_queryset(self):
        return super().get_queryset().filter(user__id=self.request.user.id)

class StudyGuideUpdateView(LoginRequiredMixin, UpdateView):
    model = models.StudyGuide
    fields = ["title"]
    template_name_suffix = "_update"

    def get_queryset(self):
        return super().get_queryset().filter(user__id=self.request.user.id)

class StudyGuideDeleteView(LoginRequiredMixin, DeleteView):
    model = models.StudyGuide
    template_name_suffix = "_delete"
    # Can't use reverse here because of circular import and I am too lazy
    # to find out a better solution so here we go :)
    success_url = "/study-guides/list"

    def get_queryset(self):
        return super().get_queryset().filter(user__id=self.request.user.id)

class FlashCardSetDetailView(LoginRequiredMixin, DetailView):
    model = models.FlashCardSet

    def get_queryset(self):
        return super().get_queryset().filter(study_guide__user__id=self.request.user.id)