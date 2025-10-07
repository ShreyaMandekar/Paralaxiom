from django.urls import path
from . import views

urlpatterns = [
    path('matches_per_year/', views.matches_per_year),
    path('matches_won_per_team/', views.matches_won_per_team),
    path('extra_runs/<int:season>/', views.extra_runs_per_team),
    path('available_years/', views.available_years),

]

