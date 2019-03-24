from django.conf.urls import url
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, QueryDict
from rest_framework import viewsets, response, permissions
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
from boardGames.rental.models import Game, Reservation, Person
from django.http import Http404
from rest_framework import status
from boardgamegeek import BGGClient, BGGItemNotFoundError, BGGApiError

from boardGames.rental.serializers import UserSerializer, GroupSerializer, ReservationSerializer, GameSerializer, PersonSerializer


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


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows all games to be viewed or edited.
    """
    queryset = Game.objects.all()#.order_by('-title')
    serializer_class = GameSerializer
    # for game in queryset:
    #     if not game.description:
    #         try:
    #             bgg = BGGClient()
    #             g = bgg.game(game.title)
    #             game.picture_url = g.image
    #             game.description = g.description
    #             game.min_players = g.min_players
    #             game.max_players = g.max_players
    #             game.min_age = g.min_age
    #             game.playing_time = g.playing_time / 60
    #             game.score = g.rating_average
    #             game.publisher = g.designers[0]
    #             game.save()
    #         except (BGGItemNotFoundError, BGGApiError):
    #             pass
    # print("!!!!!!!!!")


class ReservationApiView(APIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_object(self, pk):
        try:
            return Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        reservation = self.get_object(pk)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)


class ReservationApiView2(APIView):
    def post(self, request, format=None):
        data = request.GET
        data2 = QueryDict('', mutable=True)
        data2.update(data)
        print(data2)
        id_person = request.GET["borrower"]
        data2["borrower"] = "http://localhost:8000/person/"+id_person+"/"
        id_game = request.GET["game"]
        data2["game"] = "http://localhost:8000/game/"+id_game+"/"
        #serializer = PersonSerializer(data=data2)
        print(data2)
        serializer = ReservationSerializer(data=data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonApiView2(APIView):
    def post(self, request, format=None):
        data=request.GET
        print(data)
        id_person = request.GET["borrower"]
        data["borrower"] = Person.objects.get(pk=id_person)
        id_game = request.GET["game"]
        data["game"] = Game.objects.get(pk=id_game)
        serializer = PersonSerializer(data=data)
        print(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GameApiView2(APIView):
    def post(self, request, format=None):
        serializer = GameSerializer(data=request.GET)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonApiView(APIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        person = self.get_object(pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)


class GameApiView(APIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get_object(self, pk):
        try:
            game = Game.objects.get(pk=pk)
            if not game.description:
                bgg = BGGClient()
                g = bgg.game(game.title)
                game.picture_url = g.image
                game.description = g.description
                game.min_players = g.min_players
                game.max_players = g.max_players
                game.min_age = g.min_age
                game.playing_time = g.playing_time / 60
                game.score = g.rating_average
                game.publisher = g.designers[0]
                game.save()
            return game
        except Game.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        game = self.get_object(pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)


