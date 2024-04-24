import os
import json
import argparse
from dotenv import load_dotenv

from pyl402.wallet import AlbyWallet
from pyl402.client import L402Client
from pyl402.token_store import MemoryTokenStore

load_dotenv()

# Create the L402 client
alby_wallet = AlbyWallet(os.getenv("ALBY_BEARER_TOKEN"))
token_store = MemoryTokenStore()
client = L402Client(wallet=alby_wallet, store=token_store)

def get_request(url):
    try:
        response = client.get(url)
        response.raise_for_status()
        print(json.dumps(response.json(), indent=4))
    except Exception as e:
        print(f"Error during GET request: {str(e)}")

def post_request(url, data):
    try:
        response = client.post(url, json=data)
        response.raise_for_status()
        print(json.dumps(response.json(), indent=4))
    except Exception as e:
        print(f"Error during POST request: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Simple CLI for HTTP operations")
    parser.add_argument('command', choices=['get', 'post'], help="Command to execute ('get' or 'post')")
    parser.add_argument('url', help="URL for the HTTP request")
    parser.add_argument('--data', type=json.loads, help="JSON data for POST requests", default={})
    args = parser.parse_args()

    if args.command == 'get':
        get_request(args.url)
    elif args.command == 'post':
        post_request(args.url, args.data)

if __name__ == '__main__':
    main()