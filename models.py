"""Data models for airdrops"""
from pydantic import BaseModel

class Airdrop(BaseModel):
    name: str
    chain: str
    deadline: str
    link: str
    status: str = "pending"
