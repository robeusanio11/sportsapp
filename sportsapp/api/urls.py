from django.urls import path
from .views import TeamView
from .models import getTeams

urlpatterns = [
    path('home', TeamView.as_view()),
    path('', TeamView.as_view()),
]