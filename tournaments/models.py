from django.db import models
from players.models import Player


class Tiebreak(models.Model):
    name = models.CharField(max_length=50)


class Tournament(models.Model):
    name = models.TextField()
    rounds_number = models.IntegerField()
    description = models.TextField()
    image = models.TextField()
    score_byes = models.FloatField(null=True)
    status = models.ForeignKey(
        "rounds.MatchStatus", on_delete=models.CASCADE, null=True
    )


class TiebreakTournament(models.Model):
    tiebreak = models.ForeignKey(Tiebreak, on_delete=models.CASCADE, null=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True)


class TournamentPlayer(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)
