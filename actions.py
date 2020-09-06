# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionWeather(Action):
	def name(self):
		return 'action_weather'

	def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		loc = tracker.get_latest_entity_values('location')

		import requests

		params = {
			'access_key':'a487f70a4f0167fd446bb3b249ff1c3c',
			'query':loc
		}

		api_result = requests.get('http://api.weatherstack.com/current', params)

		api_response = api_result.json()

		country = api_response['location']['country']
		city = api_response['location']['name']
		condition = api_response['current']['weather_descriptions'][0].lower()
		temperature = api_response['current']['temperature']
		humidity = api_response['current']['humidity']
		wind_speed = api_response['current']['wind_speed']
		feels_like = api_repsonse['current']['feelslike']

		response = """It's {} in {}, {} at the moment. The temperature is {} degrees celsius, the humidity is {} percent and the wind speed is {} kmph.""".format(condition, city, country, temperature, humidity, wind_speed)

		dispatcher.utter_message(response)

		return []

# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []
