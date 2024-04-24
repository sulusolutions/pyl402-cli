import os
from dotenv import load_dotenv

from pyl402.wallet import AlbyWallet
from pyl402.client import L402Client
from pyl402.token_store import MemoryTokenStore

load_dotenv()

# Create the L402 client
alby_wallet = AlbyWallet(os.getenv("ALBY_BEARER_TOKEN"))
token_store = MemoryTokenStore()
client = L402Client(wallet=alby_wallet, store=token_store)

