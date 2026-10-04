from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.generics import get_object_or_404

from players.models import Player
from players.serializers import PlayerSerializer


@api_view(["GET", "POST"])
def list_players(request: Request):
    if request.method == "GET":
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)

        return Response(serializer.data)

    if request.method == "POST":
        serializer = PlayerSerializer(data=request.data)
        # This returns error to client when data is incorrect (avoid use return)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def single_player(request: Request, id: int):
    # Method A: return response 404 automatically
    # player = get_object_or_404(Player, id=id)

    # Method B: handle exception and response returning manually
    try:
        player = Player.objects.get(id=id)
    except Player.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PlayerSerializer(player)

        return Response(serializer.data)

    if request.method == "PUT" or request.method == "PATCH":
        serializer = PlayerSerializer(player, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK)

    if request.method == "DELETE":
        player.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
