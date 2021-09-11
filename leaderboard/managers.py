from django.db import models


class PlayerManager(models.Manager):
    def __init__(self, **kwargs):
        super().__init__()
        self.annotations = kwargs

    def get_queryset(self):
        return super().get_queryset().annotate(**self.annotations)

    # def get_queryset(self):
    #     return super().get_queryset.annotate(
    #         total = F('event01') + F('event02') + F('event01') + 
    #         F('event02') + F('event01') + F('event02') +
    #         F('event01') + F('event02') + F('event01') +
    #         F('event02') + F('event01') + F('event02')
    #     )
