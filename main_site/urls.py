from django.urls import path

from main_site import views

urlpatterns = [
    path('', views.MainView.as_view(), name="home"),
    path('contact/', views.ContactView.as_view(), name="Contact"),
]
