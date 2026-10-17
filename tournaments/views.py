from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import status

from .serializers import TournamentSerializer, TournamentPlayerSerializer
from .models import Tournament, TournamentPlayer
from rounds.serializers import RoundSerializer
from rounds.models import Round, MatchStatus
from players.helpers import validate_players_exist


class ListTournamentsView(APIView):
    def post(self, request: Request):
        if not isinstance(request.data, dict):
            return Response({"message": "request must be a valid JSON object"}, status=400)

        tournament_request = request.data.get("tournament")
        players_request: list[int] | None = request.data.get("players")

        if tournament_request == None or players_request == None:
            return Response({"message": "missing tournament or player fields"}, status=400)

        is_valid_players = validate_players_exist(players_request)

        if not is_valid_players:
            return Response(
                data={"message": "one or more players do not exist"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer_tournament = TournamentSerializer(data=tournament_request)
        serializer_tournament.is_valid(raise_exception=True)
        tournament = serializer_tournament.save()

        rounds_number = tournament.rounds_number
        
        # List Comprehension
        players = [
            TournamentPlayer(
                tournament_id=tournament.id,
                player_id=player_id
            )
            for player_id in players_request
        ]
        TournamentPlayer.objects.bulk_create(players)
        serializer_players = TournamentPlayerSerializer(data=players, many=True)
        
        rounds = [
            Round(
                match_status_id=1,
                tournament=tournament,
                order=i
            )
            for i in range(0, rounds_number)
        ]
        Round.objects.bulk_create(rounds)
        serializer_rounds = RoundSerializer(rounds, many=True)

        res = {
            **serializer_tournament.data,
            "rounds": serializer_rounds.data,
            "players": serializer_players.data
        }

        return Response(res, status=201)

    def get(self, request: Request):
        tournaments = Tournament.objects.all()
        serializer = TournamentSerializer(tournaments, many=True)

        return Response(serializer.data)


