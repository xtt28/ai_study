from django.urls import path

from . import views

urlpatterns = [
    path("study-guides/new", views.StudyGuideCreateView.as_view(), name="create"),
    path("study-guides/<int:pk>/study/outline", views.StudyGuideDetailView.as_view(), name="detail"),
    path("study-guides/<int:pk>/study/flashcards", views.FlashCardSetDetailView.as_view(), name="flashcards"),
    path("study-guides/<int:pk>/study/test/multiple-choice", views.MultipleChoiceTestDetailView.as_view(), name="test_multichoice"),
    path("study-guides/<int:pk>/edit/rename", views.StudyGuideUpdateView.as_view(), name="update"),
    path("study-guides/<int:pk>/edit/delete", views.StudyGuideDeleteView.as_view(), name="delete"),
    path("study-guides/list", views.StudyGuideListView.as_view(), name="list")
]
app_name = "study_guides"