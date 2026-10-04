from django.urls import path

from . import views

urlpatterns = [
    path("players", views.list_players),
    path("players/<int:id>/", views.single_player),
]
