from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ("name",)
    search_fields = ['name']

# @admin.register(Event)
# class EventAdmin(admin.ModelAdmin):
#     list_display = ('id' ,'eventId', 'player', 'points')
#     list_filter = ("eventId",)
#     search_fields = ['eventId']