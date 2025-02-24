""" Terminal-based Country Searcher """

from requests import get

class APIError(Exception):
    """Describes an error triggered by a failing API call."""

    def __init__(self, message: str, code: int=500):
        """Creates a new APIError instance."""
        self.message = message
        self.code = code


def print_data(country_data: dict):
    """Displays country data from a dict."""
    print(country_data)


def fetch_data(country_name: str) -> dict:
    """Returns a dict of country data from the API."""
    response = get(f"https://restcountries.com/v3.1/name/{country_name.lower()}", timeout=10)
    if response.status_code == 404:
        raise APIError(message="Unable to locate matching country.", code=404)
    elif response.status_code == 500:
        raise APIError(message="Unable to connect to server.")
    elif response.status_code != 200:
        raise APIError(message=response.reason, code=response.status_code)
    data = response.json()[0]
    country_dict = {}
    country_dict['name'] = data['name']
    country_dict['flag'] = data['flag']
    country_dict['languages'] = data['languages']
    return country_dict


def main():
    """Repeatedly prompts the user for country names and displays the result."""
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
            print_data(f"{country_data['name']['official']} {
                country_data['flag']}\nLanguages: {
                    ", ".join(list(country_data['languages'].values()))}")
        except APIError as e:
            print(e.message)
        print(" ")


if __name__ == "__main__":
    main()
