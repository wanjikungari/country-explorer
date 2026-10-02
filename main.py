import requests

API_URL = "https://countries.dev/countries"


def fetch_countries():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.RequestException as error:
        print("There was a problem connecting to the Countries API.")
        print(error)
        return None


def main():
    countries = fetch_countries()

    if countries:
        print("Country data loaded successfully!")
        print(f"Number of records received: {len(countries)}")
    else:
        print("No country data was loaded.")


if __name__ == "__main__":
    main()