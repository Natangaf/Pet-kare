from django.urls import path
from .views import petsView ,petsDetailView

urlpatterns = [
    path('pets/', petsView.as_view()),
    path('pets/<int:pets_id>/', petsDetailView.as_view()),
]
