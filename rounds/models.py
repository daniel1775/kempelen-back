from players.models import Player
from django.db import models


class MatchStatus(models.Model):
    name = models.CharField(max_length=20)


class Round(models.Model):
    match_status = models.ForeignKey(
        MatchStatus, on_delete=models.CASCADE, null=True, related_name="rounds"
    )
    tournament = models.ForeignKey(
        "tournaments.Tournament",
        on_delete=models.CASCADE,
        null=True,
        related_name="rounds",
    )
    order = models.IntegerField()


class PlayerRound(models.Model):
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, null=True, related_name="player_rounds"
    )
    round = models.ForeignKey(
        Round, on_delete=models.CASCADE, null=True, related_name="player_rounds"
    )
    result = models.FloatField(null=True)
