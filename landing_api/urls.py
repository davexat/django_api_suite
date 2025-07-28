from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.LandingApi.as_view(), name='landing_api'),
]