from django.urls import path
from .views import note_page, SignIn_page, logout_page
from django.contrib.auth.decorators import login_required

app_name='UserNotes'

urlpatterns = [
    path('',login_required(note_page.as_view()),name='index'),
]
