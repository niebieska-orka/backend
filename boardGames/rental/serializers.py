from django.contrib.auth.models import User, Group
from rest_framework import serializers
from boardGames.rental.models import Game, Reservation, Person


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('title', 'description', 'picture_url', 'publisher', 'score')


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservation
        fields = ('borrower', 'game', 'reservation_date', 'borrow_date', 'taken_to_home', 'game_returned')


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'surname', 'mail', 'password')


