# Weather App

## Overview
A Flask-based weather application that provides real-time weather details and a map view for cities using the [OpenWeatherMap](https://openweathermap.org/) and Google Maps APIs.

## Features

- Real-time weather details
- Map view for cities

## Technologies

- [Flask](https://flask.palletsprojects.com/)
- [OpenWeatherMap API](https://openweathermap.org/api)
- [Google Maps API](https://developers.google.com/maps/)

## Setup and Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/code-freq/weather-app.git
    cd weather-app
    ```
2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt  
    ```
4. Add your API keys for OpenWeatherMap and Google Maps in ```weather_app.py```:
    ```python
    WEATHER_API = "YOUR OPEN WEATHER MAP API KEY"
    GOOGLE_MAPS_API = "YOUR GOOGLE MAPS API KEY"
    ```
5. Run the application:
    ```terminal
    flask run
    ```
6. Visit ```http://127.0.0.1:5000``` to view the application.

## Usage

1. Enter a city name to fetch and display the weather information.
2. View additional details such as temperature, humidity, and a map showing the city's location.

## Screenshots

![screenshot](assets/screenshot_1.png)

![screenshot](assets/screenshot_2.png)

![screenshot](assets/screenshot_3.png)



