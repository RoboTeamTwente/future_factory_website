from django.urls import path

from events import views

urlpatterns = [
    path(r'<int:pk>/', views.EventDetailView.as_view(), name="event"),
]
