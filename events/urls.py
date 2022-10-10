from django.urls import path

from events import views

urlpatterns = [
    path('', views.EventsView.as_view(), name="Events"),
    path('ffwebsite/', views.FFWebsite.as_view(), name="FF Website"),
]
