from django.urls import path

from partners import views

urlpatterns = [
    path('', views.PartnerView.as_view(), name="Partners"),
]
