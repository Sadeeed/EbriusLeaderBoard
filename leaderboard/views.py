from leaderboard.models import Player
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import generic


class Index(generic.ListView):
    model = Player
    template_name = 'leaderboard/index.html'
    paginate_by = 10