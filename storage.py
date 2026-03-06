import json
import os

VAULT_FILE = "vault.json"

def load_vault():

    if not os.path.exists(VAULT_FILE):
        return {}

    with open(VAULT_FILE,"r") as file:
        return json.load(file)


def save_vault(data):

    with open(VAULT_FILE,"w") as file:
        json.dump(data,file, indent=4)

