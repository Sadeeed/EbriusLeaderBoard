from leaderboard.forms import PlayerUpdateForm
from leaderboard.models import Player
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Max


class Index(generic.ListView):
    model = Player
    template_name = 'leaderboard/index.html'
    paginate_by = 20
    ordering = ['-total']


class DashboardView(generic.UpdateView):
    model = Player
    form_class = PlayerUpdateForm
    template_name = 'leaderboard/dashboard.html'
    success_url = reverse_lazy('home')