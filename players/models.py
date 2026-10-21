from django.db import models


class Player(models.Model):
    name = models.TextField()
    elo = models.IntegerField()
    image = models.TextField(null=True)
    chess_profile = models.URLField(null=True)
    device_id = models.TextField()

    def __str__(self):
        return f"{self.name} | {self.elo} | {self.image} | {self.chess_profile} | {self.device_id}"
