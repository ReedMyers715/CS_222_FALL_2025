import json
import ssl
from urllip.request import urlopen
def main():
    state = input("Enter two-character state code: ")
    url = "https://api.weather.gov/alerts/active?area=IN"
    context = ssl._create_unverified_context()
    response = urlopen(url, context=context)
    weatherData = json.loads(response.read())
    print(len(weatherData["features"]))

main()