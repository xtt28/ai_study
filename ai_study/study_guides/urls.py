from django.urls import path

from . import views

urlpatterns = [
    path("guide/<int:pk>/", views.StudyGuideDetailView.as_view(), name="detail")
]
app_name = "study_guides"