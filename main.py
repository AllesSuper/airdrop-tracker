import typer
from models import Airdrop
from storage import load_airdrops, save_airdrops
# ... Rest unverändert

#!/usr/bin/env python
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import typer
from pydantic import BaseModel
from typing import List
from rich.console import Console
from rich.table import Table
from src.storage import load_airdrops, save_airdrops  # ← Funktioniert jetzt

app = typer.Typer()
console = Console()

class Airdrop(BaseModel):
    name: str
    chain: str
    deadline: str
    link: str
    status: str = "pending"

airdrops: List[Airdrop] = load_airdrops()

@app.command()
def add(name: str, chain: str, deadline: str, link: str):
    airdrop = Airdrop(name=name, chain=chain, deadline=deadline, link=link)
    airdrops.append(airdrop)
    save_airdrops(airdrops)
    console.print(f"✅ Added: {name} ({chain})", style="green")

@app.command()
def list_all():
    if not airdrops:
        console.print("📭 No airdrops", style="yellow")
        return
    table = Table(title="Airdrops")
    table.add_column("Name")
    table.add_column("Chain")
    table.add_column("Deadline")
    table.add_column("Status")
    for ad in airdrops:
        table.add_row(ad.name, ad.chain, ad.deadline, ad.status)
    console.print(table)
@app.command()
def filter(chain: str):
    """Filter airdrops by chain"""
    filtered = [ad for ad in airdrops if chain.lower() in ad.chain.lower()]
    if not filtered:
        console.print(f"❌ No {chain} airdrops", style="red")
        return
    table = Table(title=f"{chain} Airdrops")
    table.add_column("Name", style="cyan")
    table.add_column("Deadline")
    for ad in filtered:
        table.add_row(ad.name, ad.deadline)
    console.print(table)

if __name__ == "__main__":
    app()
@app.command()
def done(name: str):
    """Mark airdrop as completed"""
    for ad in airdrops:
        if ad.name.lower() == name.lower():
            ad.status = "done"
            save_airdrops(airdrops)
            console.print(f"✅ {name} MARKED DONE", style="bold green")
            return
    console.print(f"❌ '{name}' not found", style="red")

@app.command()
def done(name: str):
    """Mark airdrop as completed"""
    for ad in airdrops:
        if ad.name.lower() == name.lower():
            ad.status = "done"
            save_airdrops(airdrops)
            console.print(f"✅ {name} marked DONE", style="green")
            return
    console.print(f"❌ {name} not found", style="red")

