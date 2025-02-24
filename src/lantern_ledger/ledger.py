from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import csv
from typing import List

DATE_FMT = "%Y-%m-%d"

@dataclass
class Entry:
    date: datetime
    category: str
    description: str
    amount: float  # positive for income, negative for expense

    def to_row(self) -> List[str]:
        return [self.date.strftime(DATE_FMT), self.category, self.description, f"{self.amount:.2f}"]

    @staticmethod
    def header() -> List[str]:
        return ["date", "category", "description", "amount"]

class Ledger:
    def __init__(self, path: Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            with self.path.open("w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(Entry.header())

    def add(self, entry: Entry) -> None:
        with self.path.open("a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(entry.to_row())

    def load(self) -> List[Entry]:
        rows: List[Entry] = []
        if not self.path.exists():
            return rows
        with self.path.open("r", newline="") as f:
            reader = csv.DictReader(f)
            for r in reader:
                rows.append(
                    Entry(
                        date=datetime.strptime(r["date"], DATE_FMT),
                        category=r["category"],
                        description=r["description"],
                        amount=float(r["amount"]),
                    )
                )
        return rows

    def balance(self) -> float:
        return sum(e.amount for e in self.load())
