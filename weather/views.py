from django.shortcuts import render, HttpResponse
import requests

# Create your views here.
def weather(request):
    data = {}
    if request.method == 'POST':
        city = request.POST.get('city', '').strip()
        if city:
            source = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=d281be40e23a125b47beee2aa360bfaf"
            try:
                response = requests.get(source.format(city))
                list_of_data = response.json()
                
                if response.status_code == 200:
                    data = {
                        "country_code": list_of_data.get('sys', {}).get('country', ''),
                        "city": city.title(),
                        "coordinate": str(list_of_data.get('coord', {}).get('lon')) + ' ' + str(list_of_data.get('coord', {}).get('lat')),
                        "temp": list_of_data.get('main', {}).get('temp', ''),
                        "pressure": list_of_data.get('main', {}).get('pressure', ''),
                        "humidity": list_of_data.get('main', {}).get('humidity', ''),
                        "description": list_of_data.get('weather', [{}])[0].get('description', '').capitalize(),
                        "icon": list_of_data.get('weather', [{}])[0].get('icon', ''),
                        "wind_speed": list_of_data.get('wind', {}).get('speed', ''),
                    }
                    
                    # Fetch City Description from Wikipedia
                    try:
                        wiki_source = f"https://en.wikipedia.org/api/rest_v1/page/summary/{city.title()}"
                        headers = {'User-Agent': 'WeatherApp/1.0 (contact@example.com)'}
                        wiki_response = requests.get(wiki_source, headers=headers)
                        if wiki_response.status_code == 200:
                            wiki_data = wiki_response.json()
                            data["city_description"] = wiki_data.get("extract", "")
                    except Exception:
                        pass
                        
                else:
                    data = {
                        "error": list_of_data.get("message", "City not found. Please try again.").capitalize()
                    }
            except Exception as e:
                data = {
                    "error": "Failed to retrieve weather data. Please check your connection and try again."
                }
    return render(request, "weather.html", data)