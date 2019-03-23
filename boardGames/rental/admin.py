from django.contrib import admin

# Register your models here.
from .models import Person, Game, Reservation

admin.site.register(Person)
admin.site.register(Game)
admin.site.register(Reservation)