## path 1
* greet
  - utter_greet
  - utter_help
* inform
  - action_weather
* thanks
  - utter_welcome
* goodbye
  - utter_goodbye

## path 2
* greet
  - utter_greet
  - utter_help
* inform_no_location
  - utter_ask_location
* inform_location
  - action_weather
* thanks
  - utter_welcome
* goodbye
  - utter_goodbye

## path 3
* greet
  - utter_greet
  - utter_help
* inform_no_location
  - utter_ask_location
* inform_location
  - action_weather
* thanks
  - utter_welcome
* bot_challenge
  - utter_iamabot
* goodbye
  - utter_goodbye

## path 4
* greet
  - utter_greet
  - utter_help
* goodbye
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## ask for humidity
* greet
  - utter_greet
  - utter_help
* inform_location
  - action_weather
* inform_humidity
  - action_humidity
* thanks
  - utter_welcome

## ask for wind_speed
* greet
  - utter_greet
  - utter_help
* inform_location
  - action_weather
* inform_wind_speed
  - action_wind_speed
* thanks
  - utter_welcome

## ask for humidity and wind_speed
* greet
  - utter_greet
  - utter_help
* inform_location
  - action_weather
* inform_humidity
  - action_humidity
* inform_wind_speed
  - action_wind_speed
* thanks
  - utter_welcome

## interactive_story_1
* greet
    - utter_greet
    - utter_help
* inform{"location": "London"}
    - action_weather
* thanks
    - utter_welcome
* inform{"location": "Kingston"}
    - action_weather
* thanks
    - utter_welcome
* bot_challenge
    - utter_iamabot
* out_of_scope
    - utter_out_of_scope
* no_response_required
* inform{"location": "Rotterdam"}
    - action_weather
* thanks
    - utter_welcome

## interactive_story_1
* greet
    - utter_greet
    - utter_help
* inform_no_location
    - utter_ask_location
* inform_location{"location": "Pune"}
    - action_weather
* no_response_required
* inform{"location": "amsterdam"}
    - action_weather
* no_response_required
* out_of_scope
    - utter_out_of_scope
* creator_challenge
    - utter_creator_challenge
* no_response_required
* inform_no_location{"location": "Berlin"}
    - action_weather
* inform{"location": "Barcelona"}
    - action_weather
* inform{"location": "Ottawa"}
    - action_weather
* inform{"location": "Montreal"}
    - action_weather
* no_response_required
* thanks
    - utter_welcome
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
    - utter_help

## interactive_story_2
* greet
    - utter_greet
    - utter_help
* inform{"location": "London"}
    - action_weather
* thanks
    - utter_welcome
    - utter_default
* out_of_scope
    - utter_out_of_scope
* creator_challenge
    - utter_creator_challenge
* bot_challenge
    - utter_iamabot
* no_response_required
* no_response_required
* inform{"location": "Pretoria"}
    - action_weather
* thanks
    - utter_welcome
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
    - utter_help
* inform_no_location
    - utter_ask_location
* inform_location{"location": "Budapest"}
    - slot{"location": "Budapest"}
    - action_weather
* inform_humidity
    - action_humidity
    - slot{"location": "Budapest"}
* inform_wind_speed
    - action_wind_speed
* no_response_required
* thanks
    - utter_welcome
