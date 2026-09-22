from players.models import Player
from django.db import models


class MatchStatus(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"


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

    def __str__(self):
        return f"{self.match_status} | {self.tournament} | {self.order}"


class PlayerRound(models.Model):
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, null=True, related_name="player_rounds"
    )
    round = models.ForeignKey(
        Round, on_delete=models.CASCADE, null=True, related_name="player_rounds"
    )
    result = models.FloatField(null=True)

    def __str__(self):
        return f"{self.player} | {self.round} | {self.result}"
