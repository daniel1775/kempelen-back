from django.db import models


class Player(models.Model):
    name = models.TextField()
    elo = models.IntegerField(null=True)
    image = models.TextField(null=True)
    chess_profile = models.URLField(null=True)

    def __str__(self):
        return f"{self.name} | {self.elo} | {self.image} | {self.chess_profile}"
