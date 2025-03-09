from pathlib import Path
from datetime import datetime
from lantern_ledger.ledger import Ledger, Entry

def test_balance_and_roundtrip(tmp_path: Path):
    db = tmp_path/"ledger.csv"
    l = Ledger(db)
    l.add(Entry(datetime(2025,1,1), "salary", "jan", 1000.0))
    l.add(Entry(datetime(2025,1,2), "food", "lunch", -12.55))
    assert abs(l.balance() - 987.45) < 1e-6
    rows = l.load()
    assert len(rows) == 2
    assert rows[0].category == "salary"
