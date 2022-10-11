from django.urls import path

from teams import views

urlpatterns = [
 path(r'<int:pk>/', views.TeamDetailView.as_view(), name="team"),
 path('dtt/', views.DroneTeamView.as_view(), name="Drone Team Twente"),
 path('est/', views.ElectricSuperBikeView.as_view(), name="Electric Superbike Twente"),
 path('gtt/', views.GreenTeamView.as_view(), name="Green Team Twente"),
 path('rtt/', views.RoboTeamView.as_view(), name="RoboTeam Twente"),
 path('sbt/', views.SolarBoatView.as_view(), name="Solar Boat Twente"),
]
