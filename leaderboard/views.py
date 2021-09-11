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

    # def get_context_data(self, **kwargs):
    #     print(self.get_object())
    #     return super().get_context_data(**kwargs)
    
    # def get_object(self, queryset=None):
    #     oldObj = super().get_object(queryset=queryset)
    #     playerObj = Player.objects.filter(pk = self.kwargs.get('pk'))
    #     playerEvents = Event.objects.filter(player=playerObj)                                                                                                   
    #     return playerEvents