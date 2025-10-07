from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Match, Delivery
from .serializers import MatchSerializer, DeliverySerializer
from django.db.models import Count, Sum

# 1. Matches per year
@api_view(['GET'])
def matches_per_year(request):
    data = Match.objects.values('season').annotate(count=Count('match_id')).order_by('season')
    return Response(list(data))

# 2. Matches won per team
@api_view(['GET'])
def matches_won_per_team(request):
    data = Match.objects.values('winner').annotate(count=Count('match_id')).order_by('winner')
    return Response(list(data))

# 3. Extra runs per team for a given season
@api_view(['GET'])
def extra_runs_per_team(request, season):
    matches = Match.objects.filter(season=season).values_list('match_id', flat=True)
    data = Delivery.objects.filter(match_id__in=matches)\
        .values('bowling_team')\
        .annotate(extra=Sum('extra_runs'))\
        .order_by('bowling_team')
    return Response(list(data))

@api_view(['GET'])
def available_years(request):
    years = list(Match.objects.values_list('season', flat=True).distinct().order_by('season'))
    return JsonResponse(years, safe=False)
