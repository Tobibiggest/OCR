from django.urls import path
from .views import upload_file
from . import views

urlpatterns = [
    path("upload/", upload_file, name="upload"),
    path('', views.home, name='home'),
    path('download-csv/', views.download_csv, name='download_csv'),
    
]
