from django.urls import path

from main_site import views

urlpatterns = [
    path('', views.MainView.as_view(), name="home"),
    path('press/', views.PressView.as_view(), name="press"),
    path('send_email/', views.SendMessage.as_view(), name="send_message"),
]
