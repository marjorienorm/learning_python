import requests


def get_weather_description_and_temp( city ):
    api_key = "e71837004f5f885492bf461238cc822e"
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "&units=imperial"

    request = requests.get( url) 
    json = request.json()
    #print( json )

    description = json.get("weather")[0].get("description")

    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {'description': description,
            'temp_min': temp_min,
            'temp_max': temp_max}


def main():
    # Print the results
    weather_info = get_weather_description_and_temp("Flower Mound")

    print( "Today's forcast is ", weather_info.get('description'), ", the minimum temperature is ", weather_info.get('temp_min'), " with a max of ", weather_info.get('temp_max'), ".", sep='')

main()