#!/usr/bin/env python
"""
Airdrop Tracker CLI - Track your crypto airdrops efficiently
"""

import typer
from pydantic import BaseModel
from typing import List, Optional
from rich.console import Console
from rich.table import Table
import json
import os

app = typer.Typer()
console = Console()

class Airdrop(BaseModel):
    name: str
    chain: str
    deadline: str
    link: str
    status: str = "pending"

# In-memory storage (later file/DB)
airdrops: List[Airdrop] = []

@app.command()
def add(name: str, chain: str, deadline: str, link: str):
    """Add a new airdrop"""
    airdrop = Airdrop(name=name, chain=chain, deadline=deadline, link=link)
    airdrops.append(airdrop)
    console.print(f"✅ Added: {name} on {chain}", style="green")

@app.command()
def list_all():
    """List all airdrops"""
    if not airdrops:
        console.print("📭 No airdrops yet", style="yellow")
        return
    
    table = Table(title="Your Airdrops")
    table.add_column("Name")
    table.add_column("Chain")
    table.add_column("Deadline")
    table.add_column("Status")
    
    for airdrop in airdrops:
        table.add_row(airdrop.name, airdrop.chain, airdrop.deadline, airdrop.status)
    
    console.print(table)

if __name__ == "__main__":
    app()
