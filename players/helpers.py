from .models import Player

def validate_players_exist(list_players: list[int]):
    try:
        for player_id in list_players:
            Player.objects.get(id=player_id)

        return True
    except Player.DoesNotExist:
        return False