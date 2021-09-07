from django.db import models
from mojang import MojangAPI


class Player(models.Model):
    name = models.CharField(max_length=256)
    uuid = models.CharField(max_length=32, default='44e3cb79f8e84721ade0831761b0e40c')
    imageUrl = models.URLField(default='google.com')


    def save(self, *args, **kwargs):
        if self.name:
            self.uuid = MojangAPI.get_uuid(self.name)
            self.imageUrl = (f"https://www.mc-heads.net/avatar/{self.uuid}/32")
        return super().save(self, *args, **kwargs)

    def __str__(self):
        return self.name


class Event(models.Model):
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='events')
    eventId = models.IntegerField()
    points = models.IntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.eventId)