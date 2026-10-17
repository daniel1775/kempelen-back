from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from .serializers import TournamentSerializer
from rounds.serializers import RoundSerializer
from .models import Tournament
from rounds.models import Round, MatchStatus


class ListTournamentsView(APIView):
    def post(self, request: Request):
        serializer_tournament = TournamentSerializer(data=request.data)
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


