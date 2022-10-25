from django.urls import path

from teams import views

urlpatterns = [
 # path('<int:pk>/', views.TeamDetailView.as_view(), name="team"),
 path('<slug:slug>/', views.TeamDetailView.as_view(), name="team"),
]
