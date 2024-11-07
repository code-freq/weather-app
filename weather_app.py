import requests
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

WEATHER_API = "YOUR OPEN WEATHER MAP API KEY"
MAPS_API = "YOUR GOOGLE MAPS API KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def direction(deg):
    if 0 <= deg < 22.5 or 157.5 <= deg <= 180:
        return "N"
    elif 22.5 <= deg < 67.5:
        return "NE"
    elif 67.5 <= deg < 112.5:
        return "E"
    elif 112.5 <= deg < 157.5:
        return "SE"
    elif 157.5 <= deg < 202.5:
        return "S"
    elif 202.5 <= deg < 247.5:
        return "SW"
    elif 247.5 <= deg < 292.5:
        return "W"
    elif 292.5 <= deg < 337.5:
        return "NW"
    elif 337.5 <= deg < 360:
        return "N"

def get_weather(city):
    params = {
        "q": city,
        "appid": WEATHER_API,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        main = data["main"]

        temperature = main["temp"]
        humidity = main["humidity"]
        feels_like = main["feels_like"]
        min_temp = main["temp_min"]
        max_temp = main["temp_max"]
        pressure = main["pressure"]
        sea_level = main["sea_level"]
        grnd_level = main["grnd_level"]

        visibility = data["visibility"]

        wind_speed = data["wind"]["speed"]
        wind_deg = data["wind"]["deg"]

        cloudiness = data["clouds"]["all"]

        sunrise = data["sys"]["sunrise"]
        sunset = data["sys"]["sunset"]

        time = data["dt"]
        timezone = data["timezone"]

        weather_desc = data["weather"][0]["description"]
        name = data["name"]

        coords = data["coord"]
        lat = coords["lat"]
        lon = coords["lon"]

        weather_data = {
            "weather_desc": weather_desc,
            "temperature": temperature,
            "feels_like": feels_like,
            "min_temp": min_temp,
            "max_temp": max_temp,
            "pressure": pressure,
            "humidity": humidity,
            "sea_level": sea_level,
            "grnd_level": grnd_level,
            "visibility": visibility,
            "wind_speed": wind_speed,
            "wind_dir": direction(wind_deg),
            "cloudiness": cloudiness,
            "sunrise": datetime.fromtimestamp(sunrise + timezone - 3600*3).time(),
            "sunset": datetime.fromtimestamp(sunset + timezone - 3600*3).time(),
            "time": datetime.fromtimestamp(time + timezone - 3600*3).time(),
            "name": name,
            "lat": lat,
            "lon": lon,
            "api_key": MAPS_API
        }

        return weather_data
    else:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form["city"]
        weather_data = get_weather(city)
    return render_template("index.html", weather_data=weather_data)

if __name__ == "__main__":
    app.run(debug=True)