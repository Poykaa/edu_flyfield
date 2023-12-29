from django.urls import path
from . import views


app_name = 'subjects'

urlpatterns = [
    path('<slug:subject_slug>', views.get_subject, name='subject')
]