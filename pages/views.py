import requests
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

class WeatherPageView(TemplateView):
    template_name = "weather.html"

    latitude = 46.87
    longitude = -113.99

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "current": "temperature_2m,wind_speed_10m,weather_code",
            "temperature_unit": "fahrenheit",
            "wind_speed_unit": "mph",
        }

        try:
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            context["weather"] = response.json()["current"]
        except requests.RequestException:
            context["error"] = "Couldn't fetch weather right now."

        return context
