from django.urls import path

from .views import ListPlayersView, DetailPlayerView

urlpatterns = [
    path("players", ListPlayersView.as_view()),
    path("players/<int:id>/", DetailPlayerView.as_view()),
]
