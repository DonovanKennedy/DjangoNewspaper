from django.urls import path
from .views import HomePageView, WeatherPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("weather/", WeatherPageView.as_view(), name="weather")
]