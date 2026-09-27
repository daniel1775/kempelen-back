from tournaments.models import (
    Tournament,
    Tiebreak,
    TiebreakTournament,
    TournamentPlayer,
)
from rest_framework import serializers


class TiebreakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiebreak
        fields = ["id", "name"]


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


class TiebreakTournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiebreakTournament
        fields = ["id", "tiebreak", "tournament"]


class TournamentPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentPlayer
        fields = ["id", "tournament", "player"]
