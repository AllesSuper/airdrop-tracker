"""Simple JSON storage for airdrops"""
import json
import os
from typing import List
from .models import Airdrop

STORAGE_FILE = "airdrops.json"

def load_airdrops() -> List[Airdrop]:
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "r") as f:
            data = json.load(f)
            return [Airdrop(**item) for item in data]
    return []

def save_airdrops(airdrops: List[Airdrop]):
    with open(STORAGE_FILE, "w") as f:
        json.dump([adrop.dict() for adrop in airdrops], f, indent=2)
