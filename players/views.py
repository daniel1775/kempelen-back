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
        # This returns error to client when data is incorrect (avoid use of return)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT"])
def single_player(request: Request, id: int):
    if request.method == "GET":
        try:
            player = Player.objects.get(id=id)
        except Player.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PlayerSerializer(player)
        return Response(serializer.data)

    if request.method == "PUT":
        player = get_object_or_404(Player, id=id)

        serializer = PlayerSerializer(player, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK)
