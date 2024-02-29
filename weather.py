import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = 'WTAJYD7ASE5PCTXAB2PWY49ES'  # Your API key for the weather service

@app.route('/')
def index():
    """ saves the root of my app"""
    return render_template('index.html')  # Render the initial form for location input

@app.route('/forecast', methods=['POST'])
def forecast():
    """taking the data from the api and uploads it to my site"""
    location = request.form['location']  # Retrieve the location from the form input
    # Construct the API URL with the location and API key
    api_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/next6days?unitGroup=metric&include=days&key={API_KEY}&contentType=json"

    response = requests.get(api_url)  # Make a GET request to the API
    if response.status_code == 200:  # Check if the response from the API is OK
        weather_data = response.json()  # Parse the JSON response

        # Process each day's forecast from the response and store the relevant data
        daily_forecasts = [{
            'date': day['datetime'],
            'tempmax': day['tempmax'],
            'tempmin': day['tempmin'],
            'conditions': day['conditions'],
            'humidity': day['humidity'],
            'windspeed': day['windspeed'],
            'icon': day['icon'],
        } for day in weather_data.get('days', [])]  # Limit to 7 days of forecasts

        # Prepare the data dictionary to pass to the rendering context
        forecast_data = {
            'location': weather_data.get('resolvedAddress', 'Unknown'),
            'daily_forecasts': daily_forecasts,
        }
    else:
        # Handle the case where the API call was unsuccessful
        forecast_data = {
            'location': "ERROR, INVALID COUNTRY/CITY",
            'daily_forecasts': [],  # Provide an empty list for daily forecasts
        }
    # Render the forecast page with the collected data
    return render_template('forecast.html', data=forecast_data)

# Run the Flask app with debugging enabled and on all interfaces at port 5000
if __name__ == '__main__':
    """if main run the app"""
    app.run(host='0.0.0.0', port=80)	
    
