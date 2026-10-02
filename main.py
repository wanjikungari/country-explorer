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


def process_country(country):
    languages = country.get("languages", [])

    language_names = []

    for language in languages:
        language_names.append(language.get("name", "Unknown"))

    return {
        "name": country.get("name", "Unknown"),
        "capital": country.get("capital", "Unknown"),
        "region": country.get("region", "Unknown"),
        "population": country.get("population", "Unknown"),
        "area": country.get("area", "Unknown"),
        "languages": ", ".join(language_names)
    }


def main():
    countries = fetch_countries()

    if countries:
        first_country = process_country(countries[0])

        print("Processed country information:")
        print(first_country)

    else:
        print("No country data was loaded.")


if __name__ == "__main__":
    main()