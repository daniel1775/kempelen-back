from django.urls import path

from .views import ListTournamentsView

urlpatterns = [
    path("tournaments", ListTournamentsView.as_view())
]