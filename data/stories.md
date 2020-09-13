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

## interactive_story_2
* greet
    - utter_greet
    - utter_help
* inform{"location": "London"}
    - action_weather
* thanks
    - utter_welcome
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

## interactive_story_1
* greet
    - utter_greet
    - utter_help
* inform_no_location
    - utter_ask_location
* inform_location{"location": "Montreal"}
    - slot{"location": "Montreal"}
    - action_weather
* inform_wind_speed
    - action_wind_speed
* inform_humidity
    - action_humidity
    - slot{"location": "Montreal"}
* thanks
    - utter_welcome
* inform_no_location
    - utter_ask_location
* inform_location{"location": "Austin"}
    - slot{"location": "Austin"}
    - action_weather
* inform_humidity
    - action_humidity
    - slot{"location": "Austin"}
* inform_wind_speed
    - action_wind_speed
* no_response_required
* thanks
    - utter_welcome
* inform_no_location
    - utter_ask_location
* inform_location{"location": "Lagos"}
    - slot{"location": "Lagos"}
    - action_weather
* inform_humidity
    - action_humidity
    - slot{"location": "Lagos"}
* no_response_required
* thanks
    - utter_welcome
* inform{"location": "Seoul"}
    - slot{"location": "Seoul"}
    - action_weather
* inform_wind_speed
    - action_wind_speed
* inform_humidity{"location": "Seoul"}
    - slot{"location": "Seoul"}
    - action_humidity
    - slot{"location": "Seoul"}
* no_response_required
* bot_appreciate
    - utter_bot_appreciate
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
    - utter_help
* inform_no_location
    - utter_ask_location
* no_response_required
* no_response_required
* inform_location{"location": "Beijing"}
    - slot{"location": "Beijing"}
    - action_weather
* inform_wind_speed{"location": "Beijing"}
    - slot{"location": "Beijing"}
    - action_wind_speed
* inform_humidity
    - action_humidity
    - slot{"location": "Beijing"}
* bot_appreciate
    - utter_bot_appreciate
* no_response_required
* inform{"location": "Bruges"}
    - slot{"location": "Bruges"}
    - action_weather
* bot_appreciate
    - utter_bot_appreciate
* bot_appreciate
    - utter_bot_appreciate
* inform{"location": "Bali"}
    - slot{"location": "Bali"}
    - action_weather
* no_response_required
* inform_wind_speed
    - action_wind_speed
* thanks
    - utter_welcome
* bot_appreciate
    - utter_bot_appreciate
* bot_challenge
    - utter_iamabot
* ai_takeover
    - utter_ai_takeover
* but_in_the_future
    - not_sure
* creator_challenge
    - utter_creator_challenge
* no_response_required
* thanks
    - utter_welcome
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
    - utter_help
* no_response_required
* inform{"location": "Warsaw"}
    - slot{"location": "Warsaw"}
    - action_weather
* inform_wind_speed
    - action_wind_speed
* inform_humidity
    - action_humidity
    - slot{"location": "Warsaw"}
* bot_appreciate
    - utter_bot_appreciate
* inform_no_location
    - utter_ask_location
* inform_location{"location": "Phuket"}
    - slot{"location": "Phuket"}
    - action_weather
* no_response_required
* out_of_scope
    - utter_out_of_scope
* creator_challenge
    - utter_creator_challenge
* no_response_required
* no_response_required
* inform{"location": "Delhi"}
    - slot{"location": "Delhi"}
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
* dont_understand
    - not_sure

## interactive_story_3
* greet
    - utter_greet
    - utter_help
* dont_understand
    - utter_default
* inform{"location": "Duncan"}
    - slot{"location": "Duncan"}
    - action_weather
* inform{"location": "Parksville"}
    - slot{"location": "Parksville"}
    - action_weather
* out_of_scope{"location": "Parksville"}
    - slot{"location": "Parksville"}
    - utter_out_of_scope
* out_of_scope{"location": "Parksville"}
    - slot{"location": "Parksville"}
    - utter_out_of_scope
* inform{"location": "Nanaimo"}
    - slot{"location": "Nanaimo"}
    - action_weather
* inform_humidity
    - action_humidity
    - slot{"location": "Nanaimo"}
* inform{"location": "Tokyo"}
    - slot{"location": "Tokyo"}
    - action_weather
* thanks
    - utter_welcome

## interactive_story_1
* greet
    - utter_greet
    - utter_help
* inform_no_location
    - utter_ask_location
* inform_location{"location": "Seattle"}
    - slot{"location": "Seattle"}
    - action_weather
* no_response_required
* inform{"location": "Portland"}
    - slot{"location": "Portland"}
    - action_weather
* no_response_required
* inform{"location": "Kelowna"}
    - slot{"location": "Kelowna"}
    - action_weather
* bot_appreciate
    - utter_bot_appreciate
* bot_appreciate
    - utter_bot_appreciate
* inform_humidity{"location": "Kamloops"}
    - slot{"location": "Kamloops"}
    - action_humidity
    - slot{"location": "Kamloops"}
* thanks
    - utter_welcome
* bot_appreciate
    - utter_bot_appreciate
* bot_challenge
    - utter_iamabot
* ai_takeover
    - utter_ai_takeover
* but_in_the_future
    - not_sure

## interactive_story_1
* greet
    - utter_greet
    - utter_help
* inform{"location": "Edmonton"}
    - slot{"location": "Edmonton"}
    - action_weather
* inform_humidity
    - action_humidity
    - slot{"location": "Edmonton"}
* feature_not_implemented_yet
    - utter_feature_not_implemented_yet
* thanks
    - utter_welcome
* inform{"location": "San Francisco"}
    - slot{"location": "San Francisco"}
    - action_weather
* inform{"location": "Los Angeles"}
    - slot{"location": "Los Angeles"}
    - action_weather
* bot_appreciate
    - utter_bot_appreciate
