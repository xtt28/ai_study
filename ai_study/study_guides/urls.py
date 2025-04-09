from django.urls import path

from . import views

urlpatterns = [
    path("guide/new", views.StudyGuideCreateView.as_view(), name="create"),
    path("guide/<int:pk>/", views.StudyGuideDetailView.as_view(), name="detail")
]
app_name = "study_guides"