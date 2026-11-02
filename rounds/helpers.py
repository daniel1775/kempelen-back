from players.models import Player
from .models import Round, PlayerRound

def calculate_first_round(list_players: list[Player], firstRound: Round):
    players_ordered = sorted(list_players, key=lambda player: player.elo, reverse=True)

    mid = len(players_ordered) // 2

    top_half = players_ordered[:mid]
    bottom_half = players_ordered[mid:]

    PlayerRound()


