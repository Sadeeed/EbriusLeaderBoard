from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=256)
    uuid = models.CharField(max_length=32, default='')
    imageUrl = models.URLField(default='')

    def __str__(self):
        return self.name


class Event(models.Model):
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='comments')
    eventId = models.IntegerField()
    points = models.IntegerField()

    def __str__(self):
        return str(self.eventId)