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
def search_country(countries, search_term):
    search_term = search_term.lower()

    for country in countries:
        if country.get("name", "").lower() == search_term:
            return process_country(country)

    return None
def display_country(country):
    print("\n COUNTRY INFORMATION ")
    print(f"Name: {country['name']}")
    print(f"Capital: {country['capital']}")
    print(f"Region: {country['region']}")
    print(f"Population: {country['population']:,}")
    print(f"Area: {country['area']:,} km²")
    print(f"Languages: {country['languages']}")
def main():
    countries = fetch_countries()

    if not countries:
        print("No country data was loaded.")
        return

    while True:
        print("\n COUNTRY EXPLORER ")
        print("1. Search for a country")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter country name: ")

            if not name:
                print("Please enter a country name.")
                continue

            result = search_country(countries, name)

            if result:
                display_country(result)
            else:
                print("Country not found.")

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()