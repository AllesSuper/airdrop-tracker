"""Data models for airdrops"""
from pydantic import BaseModel
from typing import Optional

class Airdrop(BaseModel):
    name: str
    chain: str
    deadline: str
    link: str
    status: str = "pending"
    
    class Config:
        arbitrary_types_allowed = True
