from tournaments.models import Tournament
from rest_framework import serializers


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = [
            "id",
            "name",
            "rounds_number",
            "description",
            "image",
            "score_byes",
            "status",
        ]
