from django.db import models
import requests

def getTeams():
    teams = requests.get('https://www.balldontlie.io/api/v1/teams').json()['data']
    for team in teams:
        newTeam = Team(id = team['id'], 
                       abbreviation = team['abbreviation'],
                       city = team['city'],
                       conference = team['conference'],
                       division = team['division'],
                       full_name = team['full_name'],
                       name = team['name'])
        newTeam.save()
    Team.objects.all().values()

# Create your models here.
class Team(models.Model):
    abbreviation = models.CharField(max_length=5)
    city = models.CharField(max_length=25)
    conference = models.CharField(max_length= 15)
    division = models.CharField(max_length=15)
    full_name = models.CharField(max_length=50)
    name = models.CharField(max_length=25)