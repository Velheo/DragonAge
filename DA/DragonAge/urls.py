from django.urls import path
from . import views

app_name="DragonAge"

urlpatterns=[
    path('', views.index, name="index"),
    #path('game/<int:pk>/', views.game_detail, name="game_detail"),
    path('game/<int:pk>/', views.GameDetailView.as_view(), name="game_detail"),
    #path('race/', views.race_list, name="race_list"),
    path('race/', views.RaceListView.as_view(), name="race_list"),
    #path('classes/', views.clasess_list, name="clasess_list"),
    path('class/', views.ClasessListView.as_view(), name="clasess_list"),
    #path('locations/', views.Locations_list, name="Locations_list"),
    path('locations/', views.LocationsListView.as_view(), name="Locations_list"),
    path('companion/', views.Companion_list, name="Companion_list"),
    #path('companions/', views.CompanionListView.as_view(), name="Companion_list"),
    #path('companions/<int:pk>/', views.Companion_detail, name="Companion_detail"),
    path('companion/<int:pk>/', views.CompanionDetailView.as_view(), name="Companion_detail"),
    path('search/', views.search, name="search"),
]
