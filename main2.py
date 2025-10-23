import google.generativeai as genai
import requests
import json
import os  

GEMINI_API_KEY = "AIzaSyB1MlJELy7RZmnfHO1KIZBOWQCKAGV16Do"
WEATHER_API_KEY = "5ff7bbb8eaadffe49d08ece4f5644a7b"
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"  


genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

def get_weather(location):
    params = {
        'q': location,
        'appid': WEATHER_API_KEY,
        'units': 'metric' 
    }
    try:
        response = requests.get(WEATHER_API_URL, params=params)
        response.raise_for_status()  
        weather_data = response.json()
        if weather_data and weather_data.get('main'):
            temp = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            description = weather_data['weather'][0]['description']
            return f"The weather in {location} is {description} with a temperature of {temp}°C and humidity of {humidity}%."
        else:
            return "Could not retrieve weather information for that location."
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return "Sorry, there was an error getting the weather."
    except json.JSONDecodeError:
        print("Error decoding weather JSON.")
        return "Sorry, the weather data could not be processed."

def chat_with_gemini_with_weather(prompt):
    if "weather in" in prompt.lower():
        location = prompt.lower().split("weather in")[-1].strip()
        weather_info = get_weather(location)
        return weather_info
    else:
        try:
            response = model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            print(f"An error occurred with Gemini: {e}")
            return "Sorry, there was an error processing your request."

if __name__ == "__main__":
    print("Bot: Hello! Ask me anything, or ask about the weather (e.g., 'weather in Delhi').")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Bot: Goodbye!")
            break
        response = chat_with_gemini_with_weather(user_input)
        print("Bot:", response)
