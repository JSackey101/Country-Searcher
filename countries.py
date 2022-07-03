import requests


def printData(countryData):
    print(countryData)


def fetchData(countryName):
    return {}


def main():
    print(" ")
    print("####################")
    print("Welcome to the REST Countries Searcher")
    print("####################")
    print(" ")

    while 1:
        entry = input("Search for a country: ")
        print("You searched for: " + entry)
        print("Fetching...")
        print(" ")
        countryData = fetchData(entry)
        printData(countryData)
        print(" ")


main()
