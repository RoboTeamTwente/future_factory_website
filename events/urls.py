from django.urls import path

from events import views

urlpatterns = [
    path(r'<int:pk>/', views.EventDetailView.as_view(), name="event"),
    path('', views.EventListView.as_view(), name="events"),
]
