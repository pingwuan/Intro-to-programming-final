#Alexander Taylor
#Final Project
#Intro to Programming

#importing required modules
import requests, json

#City function for user input of city name or zipcode
def city():
        city_name = input("Enter City name or zip code: ")
        return city_name
        
#Connection Function connects to open weather api
def connection():
    api_key = "819e6d736ad9bce76f7cbda94656ed07"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city()

    #Try block to deterimine if internet connection is successful or not
    try:
        response = requests.get(complete_url)
        try:
            print("Connection Successful")
            x = response.json()
            return x
        except:
            print("Something went wrong with JSON")
    except:
        print("Connection Failed, Please check your internet connection!")

#Weather function Takes Json data from connection function and formats it into a legiable format
#Also validates the user's city field
def weather():
    x = connection()
    if x["cod"] != "404":

        y = x["main"]
 
        current_temperature = round(y["temp"] * 1.8 - 459.67)
 
        current_pressure = y["pressure"]
 
        current_humidity = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]
 
        print(" Temperature (in Fahrenheit) = " +
                        str(current_temperature) +
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidity) +
            "\n description = " +
                        str(weather_description))
 
    else:
        print("City or Zip Not Found enter another City or Zip!")

#Main function that makes calls to all the other functions
def main():
    options_list = ["1", "2", "3", "4", "5"] 
    print("Welcome to Alexander's Weather exchange!")
    for x_main in options_list:
        x_main = input("Please enter 1 to begin finding the weather or 2 to exit!: ")
        if x_main == "1":
            weather()
        elif x_main == "2":
            break
        elif x_main != options_list:
            input("You must pick 1 or 2 hit enter to continue: ")

#Start of call
main()
