import requests


def print_data(country_data):
    pass

def fetch_data(countryName):
    return {}


def main():
    print(" ")
    print("####################")
    print("Welcome to the REST Countries Searcher")
    print("####################")
    print(" ")

    while 1:
        entry = input("Search for a country: ")
        print(f"You searched for: {entry}")
        print("Fetching...")
        print(" ")
        try:
            country_data = fetch_data(entry)
            print_data(country_data)
        except Exception as e:
            print(e.args[0])
        print(" ")

if __name__ == "__main__":
    main()
