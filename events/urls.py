from django.urls import path

from events import views

urlpatterns = [
    path('', views.EventListView.as_view(), name="events"),
    path(r'<int:pk>/', views.EventDetailView.as_view(), name="event"),
    # path('ffwebsite/', views.FFWebsite.as_view(), name="FF Website"),
]
