from leaderboard.managers import PlayerManager
from django.db import models
from django.db.models import F
from mojang import MojangAPI


class Player(models.Model):
    name = models.CharField(max_length=256)
    uuid = models.CharField(
        max_length=32, blank=True)
    imageUrl = models.URLField(default='https://www.mc-heads.net/avatar/MHF_Steve/32')
    event01 = models.IntegerField(default=0)
    event02 = models.IntegerField(default=0)
    event03 = models.IntegerField(default=0)
    event04 = models.IntegerField(default=0)
    event05 = models.IntegerField(default=0)
    event06 = models.IntegerField(default=0)
    event07 = models.IntegerField(default=0)
    event08 = models.IntegerField(default=0)
    event09 = models.IntegerField(default=0)
    event10 = models.IntegerField(default=0)
    event11 = models.IntegerField(default=0)
    event12 = models.IntegerField(default=0)
    _total = None

    objects = PlayerManager(
        total=F('event01') + F('event02') + F('event03') +
        F('event04') + F('event05') + F('event06') +
        F('event07') + F('event08') + F('event09') +
        F('event10') + F('event11') + F('event12'),
    )

    def save(self, *args, **kwargs):
        if self.name:
            self.uuid = MojangAPI.get_uuid(self.name)
            self.imageUrl = (f"https://www.mc-heads.net/avatar/{self.uuid}/32")
        return super().save(self, *args, **kwargs)

    def __str__(self):
        return self.name

# class Event(models.Model):
#     player = models.ForeignKey(
#         Player, on_delete=models.CASCADE, related_name='events')
#     eventId = models.IntegerField()
#     points = models.IntegerField()

#     class Meta:
#         ordering = ['id']

#     def __str__(self):
#         return str(self.eventId)
