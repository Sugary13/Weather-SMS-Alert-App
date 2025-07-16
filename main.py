import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "TU_API_KEY_DE_OPENWEATHER"
LAT = TU_LATITUD
LON = TU_LONGITUD
account_sid = "TU_TWILIO_ACCOUNT_SID"
auth_token = "TU_AUTH_TOKEN"


weather_params = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "cnt": 4,

}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

data = response.json()

weather_data = data['list']


umbrella_needed = any(hour["weather"][0]["id"] < 700 for hour in weather_data)

if umbrella_needed:
    client = Client(account_sid, auth_token)
    message = client.messages.create(

        messaging_service_sid='TU_MESSAGING_SERVICE_SD',
        body='🌧️ Va a llover hoy, recuerda traer paraguas.',
        to='TU_NUMERO_TELEFONICO'
    )

    print(message.status)
