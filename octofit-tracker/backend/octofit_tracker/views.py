from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import User, Team, Activity, Leaderboard, Workout

# Set your Codespace URL here (update as needed)
CODESPACE_URL = "https://special-computing-machine-69grp4qgwggphr75g-8000.app.github.dev/"
LOCAL_URL = "http://localhost:8000/"

@api_view(['GET'])
def api_root(request, format=None):
    # Return both Codespace and localhost URLs for API endpoints
    return Response({
        'users_codespace': CODESPACE_URL + 'api/users/?format=api',
        'users_local': LOCAL_URL + 'api/users/?format=api',
        'teams_codespace': CODESPACE_URL + 'api/teams/?format=api',
        'teams_local': LOCAL_URL + 'api/teams/?format=api',
        'activities_codespace': CODESPACE_URL + 'api/activities/?format=api',
        'activities_local': LOCAL_URL + 'api/activities/?format=api',
        'leaderboard_codespace': CODESPACE_URL + 'api/leaderboard/?format=api',
        'leaderboard_local': LOCAL_URL + 'api/leaderboard/?format=api',
        'workouts_codespace': CODESPACE_URL + 'api/workouts/?format=api',
        'workouts_local': LOCAL_URL + 'api/workouts/?format=api',
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
