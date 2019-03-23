from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from rest_framework import viewsets, response

from boardGames.rental.models import Game
from boardGames.rental.serializers import UserSerializer, GroupSerializer, GameSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def games(request):
    return response()


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GamesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
