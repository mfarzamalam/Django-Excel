from django.urls import path
from .views import HomeView, upload_file

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('upload/', upload_file, name="upload")
]
