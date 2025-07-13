import requests

APi_KEY = "5a887603d93f4b99ab7d872cfc9d63b6"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
SECOND_URL="https://api.openweathermap.org/data/3.0/onecall/overview"

def fetch_weather(city):
    try:
        params = {
            "appid":APi_KEY,
            "q":city,
            "units": "metric",
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"This error happend while fetching {e}")
    
def main():
    while True:
        print("\n Welcome to weather forcast app, please choose :")
        print("1. fetch forcast")
        print("2. view Analysis")
        print("3. exit")
        
        choise = input(" please choose the task : ")
        data = {}
        if choise == "1":
            city = input("Please enter the city name : ")
            data = fetch_weather(city)
            print("the current weather of city is : ", data["weather"][0]["description"])
            print(data)
        if choise == "2":
            if len(data) > 0:
                print(data)
            else:
                print("There is nothing to show yet, please first fetch the data ...")
        if choise == "3":
            print("BYEEEE")
            break
        else:
            print("try another time")

if __name__ == "__main__":
    main()
