from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from .serializers import TournamentSerializer
from rounds.serializers import RoundSerializer
from .models import Tournament
from rounds.models import Round, MatchStatus


class ListTournamentsView(APIView):
    def post(self, request: Request):
        if not isinstance(request.data, dict):
            return Response({"message": "request must be a valid JSON object"}, status=400)

        tournament_request = request.data.get("tournament")
        players_request = request.data.get("players")

        if tournament_request == None or players_request == None:
            return Response({"message": "missing tournament or player fields"}, status=400)

        serializer_tournament = TournamentSerializer(data=tournament_request)
        serializer_tournament.is_valid(raise_exception=True)
        tournament = serializer_tournament.save()
        
        rounds_number = tournament.rounds_number
        
        # List Comprehension
        rounds = [
            Round(
                match_status_id=1,
                tournament=tournament,
                order=i
            )
            for i in range(0, rounds_number)
        ]
        Round.objects.bulk_create(rounds)
        serializer_round = RoundSerializer(rounds, many=True)

        res = {
            **serializer_tournament.data,
            "rounds": serializer_round.data
        }

        return Response(res, status=201)

    def get(self, request: Request):
        tournaments = Tournament.objects.all()
        serializer = TournamentSerializer(tournaments, many=True)

        return Response(serializer.data)


