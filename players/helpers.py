from .models import Player

def validate_players_exist(list_players: list[int]):
    try:
        res = []
        for player_id in list_players:
            player = Player.objects.get(id=player_id)
            res.append(player)

        return res
    except Player.DoesNotExist:
        return None




