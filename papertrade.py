import os
from dotenv import load_dotenv  # pip install python-dotenv

import cbpro    # pip install cbpro
import base64
import json

# initialize APIs and objects
API_KEY = os.environ.get("CBPROSAND_API_KEY")
SECRET = os.environ.get("CBPROSAND_SECRET")
PASSPHRASE = os.environ.get("CBPROSAND_PASSPHRASE")

encoded = json.dumps(SECRET).encode()
b64_secret = base64.b64encode(encoded)

auth_client = cbpro.AuthenticatedClient(key=API_KEY, b64secret=b64_secret, passphrase=PASSPHRASE)
cbpro_client = cbpro.PublicClient()


print(cbpro_client)