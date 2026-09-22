from django.db import models
from players.models import Player


class Tiebreak(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Tournament(models.Model):
    name = models.TextField()
    rounds_number = models.IntegerField()
    description = models.TextField()
    image = models.TextField()
    score_byes = models.FloatField(null=True)
    status = models.ForeignKey(
        "rounds.MatchStatus", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return f"{self.name} | {self.rounds_number} | {self.description} | {self.image} | {self.score_byes} | {self.status}"


class TiebreakTournament(models.Model):
    tiebreak = models.ForeignKey(Tiebreak, on_delete=models.CASCADE, null=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.tiebreak} | {self.tournament}"


class TournamentPlayer(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.tournament} | {self.player}"
