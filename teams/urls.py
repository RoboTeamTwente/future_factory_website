from django.urls import path

from teams import views

urlpatterns = [
 path('<slug:slug>/', views.TeamDetailView.as_view(), name="team"),
]
