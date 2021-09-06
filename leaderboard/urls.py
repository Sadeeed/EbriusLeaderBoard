from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
]
