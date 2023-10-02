from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'abbreviation', 'city', 'conference', 'division', 'full_name', 'name')