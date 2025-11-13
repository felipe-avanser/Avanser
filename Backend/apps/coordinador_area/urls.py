# urls de coordinador de area
from django.urls import path
from .views import InstructorCSVUploadView

urlpatterns = [
    path("upload-instructores/", InstructorCSVUploadView.as_view(), name="upload_instructores"),
]
