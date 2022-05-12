#Alexander Taylor
#Final Project
#Intro to Programming

#importing required modules
import requests, json


def city():
        city_name = input("Enter City name or zip code: ")
        return city_name

def connection():
    api_key = "819e6d736ad9bce76f7cbda94656ed07"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city()
 
    response = requests.get(complete_url)
 
    x = response.json()
    return x

def weather():
    x = connection()
    if x["cod"] != "404":

        y = x["main"]
 
        current_temperature = y["temp"]
 
        current_pressure = y["pressure"]
 
        current_humidity = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]
 
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) +
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidity) +
            "\n description = " +
                        str(weather_description))
 
    else:
        print(" City Not Found enter another City ")

def main():
    options_list = ["1", "2"]
    print("Welcome to Alexander's Weather exchange!")
    for x_main in options_list:
        x_main = input("Please enter 1 to begin find the weather or 2 to exit!: ")
        if x_main == "1":
            print(weather())
            continue
        elif x_main == "2":
            break
        elif x_main != options_list:
            input("Please enter in 1 or 2 to coninute: ")

main()

#Still working on this need to add comments and figure out why it can't keep on repeating past 3 times