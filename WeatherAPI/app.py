from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your own OpenWeatherMap API key
API_KEY = 'Your API Key Here'
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'

 #Replace /city with the city you want to get weather data for. IE) MOntreal, Barrie, Toronto, etc.

@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    # city = request.args.get('city', city)
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(WEATHER_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        return jsonify(weather)
    else:
        return jsonify({'error': 'Could not fetch weather data'}), 400

#Display the full weather data for a Toronto by default, or any city specified in the query parameter.
@app.route('/', methods=['GET'])
def full():
    city = request.args.get('city', 'Toronto')
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(WEATHER_URL, params=params)
    if response.status_code == 200:
        data = response.json()

        return jsonify(data)
    else:
        return jsonify({'error': 'Could not fetch weather data'}), 400
    
if __name__ == '__main__':
    app.run(debug=True)