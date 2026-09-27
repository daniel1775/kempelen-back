from rest_framework.response import Response
from rest_framework.decorators import api_view

from rounds.models import MatchStatus
from rounds.serializers import MatchStatusSerializer


@api_view(["GET"])
def list_match_status(request):
    status = MatchStatus.objects.all()
    serializer = MatchStatusSerializer(status, many=True)

    return Response(serializer.data)
