from django.contrib import admin
from .models import Player, Event

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'uuid')
    list_filter = ("name",)
    search_fields = ['name']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('player', 'eventId', 'points')
    list_filter = ("eventId",)
    search_fields = ['eventId']