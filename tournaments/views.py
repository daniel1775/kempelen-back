from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from .serializers import TournamentSerializer
from rounds.models import Round


class ListTournamentsView(APIView):
    def post(self, request: Request):
        serializer = TournamentSerializer(data=request.data.tournament)
        print(f"PREV: {serializer.data}")
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(f"POS: {serializer.data}")

        return Response(serializer.data)






