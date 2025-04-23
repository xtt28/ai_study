from django.urls import path

from . import views

urlpatterns = [
    path("guides/new", views.StudyGuideCreateView.as_view(), name="create"),
    path("guides/<int:pk>/overview", views.StudyGuideDetailView.as_view(), name="detail"),
    path("guides/<int:pk>/update", views.StudyGuideUpdateView.as_view(), name="update"),
    path("guides/list", views.StudyGuideListView.as_view(), name="list")
]
app_name = "study_guides"