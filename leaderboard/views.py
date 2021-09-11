from leaderboard.forms import PlayerUpdateForm
from leaderboard.models import Player
from django.views import generic


class Index(generic.ListView):
    model = Player
    template_name = 'leaderboard/index.html'
    paginate_by = 14
    ordering = ['-total']


class DashboardView(generic.UpdateView):
    model = Player
    form_class = PlayerUpdateForm
    template_name = 'leaderboard/dashboard.html'