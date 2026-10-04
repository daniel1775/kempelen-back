from django.urls import path

from . import views

urlpatterns = [path("match-status", views.list_match_status)]
