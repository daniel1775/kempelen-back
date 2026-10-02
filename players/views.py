from rest_framework.response import Response
from rest_framework.decorators import api_view

from players.models import Player
from players.serializers import PlayerSerializer


@api_view(["GET"])
def list_players(request):
    players = Player.objects.all()
    serializer = PlayerSerializer(players, many=True)

    return Response(serializer.data)
