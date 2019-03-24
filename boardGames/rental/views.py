from django.utils import timezone

from django.conf.urls import url
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, QueryDict, HttpResponseRedirect
from rest_framework import viewsets, response, permissions
from django.core import serializers
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
from boardGames.rental.models import Game, Reservation, Person
from django.http import Http404
from rest_framework import status

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
    queryset = Game.objects.all()
    serializer_class = GameSerializer


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
        print(request.GET["game"])
        person_id = request.GET["borrower"]
        game_id = request.GET["game"]
        date = request.GET["borrow_date"]
        print(person_id, game_id, date)
        print(timezone.now)
       # r = Reservation(borrow_date=date, borrower_id=person_id, game_id=game_id)
        r = Reservation(borrower=Person.objects.get(pk=person_id), game=Game.objects.get(pk=game_id), borrow_date=date)
        print(r)
        r.save()
        return HttpResponse(200)
        # data = request.GET
        # data2 = QueryDict('', mutable=True)
        # data2.update(data)
        # print(data2)
        # id_person = request.GET["borrower"]
        # data2["borrower"] = "http://localhost:8000/person/"+id_person+"/"
        # id_game = request.GET["game"]
        # data2["game"] = "http://localhost:8000/game/"+id_game+"/"
        # #serializer = PersonSerializer(data=data2)
        # print(data2)
        # serializer = ReservationSerializer(data=data2)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        reservation = self.get_object(pk)
        serializer = GameSerializer(reservation)
        return Response(serializer.data)


class GetReservationByUserApiView(APIView):
    def get(self, request, format=None):
        print(request.GET['mail'])
        user = Person.objects.get(mail__exact=request.GET['mail'])
        reservation = Reservation.objects.all().filter(borrower__mail=user.mail)
        print(reservation.__class__)
        data = serializers.serialize('json', reservation)
        return HttpResponse(data)


class AddGameApiView(APIView):
    def post(self, request, format=None):
        game_name = request.GET["title"]
        g = Game(title=game_name)
        g.save()
        return HttpResponse(200)
