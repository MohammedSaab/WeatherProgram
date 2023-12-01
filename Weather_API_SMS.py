import requests
from twilio.rest import Client

# OpenWeatherMap API Key
api_key = 'db238c9e2672ca845aad6e1cabe1f013 '

# Twilio Account SID and Auth Token
account_sid = 'ACeba86df09676a5b430d30d40a8c59916'
auth_token = 'c55c457245a3938f8a8f189c40429b9f'

# Twilio phone number (sender)
from_phone_number = '+17122183464'
# Phone number to send the SMS to (recipient)
to_phone_number = '+6465463874'
# Get the current weather for a specific city
city = 'New York'
weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
response = requests.get(weather_url)
data = response.json()

try:
    temp = data['main']['temp']
    print(temp)
except KeyError:
    print("Error: 'main' key not found in API response.")
    temp = None

try:
    condition = data['weather'][0]['main']
except KeyError:
    print("Error: 'weather' key not found in API response.")
    condition = None

if temp:
    # Convert temperature from Kelvin to Fahrenheit
    temp_f = (temp - 273.15) * 9/5 + 32
else:
    temp_f = None

# Create the message to send
message = f'The current weather in {city} is {round(temp_f)}°F and {condition}.'

# Send the SMS
client = Client(account_sid, auth_token)
message = client.messages.create(
    body=message,
    from_=from_phone_number,
    to=to_phone_number
)

print(f'SMS sent to {to_phone_number}')