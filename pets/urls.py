from django.urls import path
from .views import petsView

urlpatterns = [
    path('pets/', petsView.as_view()),
]
