from django.shortcuts import render
from rest_framework import generics
from .serializers import TeamSerializer
from .models import Team, getTeams

# Create your views here.

class TeamView(generics.CreateAPIView):
    # getTeams()
    queryset = Team.objects.all()
    serializer_class = TeamSerializer