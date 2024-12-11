import requests
import sys
import json


def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        return data["bpi"]["USD"]["rate_float"]
    except requests.RequestException as e:
        sys.exit(f"Error fetching Bitcoin price: {e}")


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")

    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: Number of bitcoins must be a float")

    price_per_bitcoin = get_bitcoin_price()
    total_cost = num_bitcoins * price_per_bitcoin

    print(f"The current cost of {num_bitcoins} Bitcoins is ${total_cost:,.4f} USD")


if __name__ == "__main__":
    main()
