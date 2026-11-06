
import requests
import requests.exceptions

country_name = input("Enter the country name: ").lower()


try:

    response = requests.get(
        f'https://api.restcountries.com/countries/v5?q={country_name}',
        headers={'Authorization': 'Bearer rc_live_9608bf72fe704b9cbc7d5aacb8259bf5'}
    )
    response.raise_for_status()
    print("Request Successful!")
    data = response.json()  # assigning the output to a variable
    countries = data["data"]["objects"]

    if not countries:
        print("Country not found!")
    else:
        country = countries[0]  # storing the dictionary in a shorter meaningful variable

        print("=============")
        print("COUNTRY INFO")
        print("=============")

        print(f'Country: {country["names"]["common"]}')  # printing the common name
        print(f'Official Name: {country["names"]["official"]}')  # printing the official name
        print(f'Capital: {country["capitals"][0]["name"]}')  # printing the capital
        print(f'Region: {country["region"]}')  # printing the region
        print(f'Population: {country["population"]:,}')  # printing the population
        print(f'Currency: {country["currencies"][0]["code"]} - {country["currencies"][0]["name"]}')  # printing the currency

except requests.exceptions.Timeout:
    print("The request took so long!")
except requests.exceptions.ConnectionError:
    print("Could not connect to the API!")
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.exceptions.RequestException as e:
    print(f"An unexpected error occurred: {e}")







