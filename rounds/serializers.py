from rest_framework import serializers
from rounds.models import Round, MatchStatus, PlayerRound
from players.serializers import PlayerSerializer


class MatchStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchStatus
        fields = ["id", "name"]


class RoundSerializer(serializers.ModelSerializer):
    match_status = MatchStatusSerializer()

    class Meta:
        model = Round
        fields = ["id", "match_status", "tournament", "order"]


class PlayerRoundSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()
    round = RoundSerializer()

    class Meta:
        model = PlayerRound
        fields = ["id", "player", "round", "result"]
