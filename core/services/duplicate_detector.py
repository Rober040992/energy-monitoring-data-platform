from __future__ import annotations
from typing import Iterable, Tuple
from core.entities.entities_energy_record import EnergyRecord

# Composite key used to identify duplicates
DuplicateKey = Tuple[str, str, str]  # (building_id, date_iso, provider)

# Builds the unique key used to detect duplicates
def get_duplicate_key(record: EnergyRecord) -> DuplicateKey:
    return (record.building_id, record.date.isoformat(), record.provider)

# Counts how many records are duplicates based on the duplicate key
def count_duplicates(records: Iterable[EnergyRecord]) -> int:
    seen: set[DuplicateKey] = set()
    duplicates = 0

    for record in records:
        key = get_duplicate_key(record)
        if key in seen:
            duplicates += 1
            continue
        seen.add(key)

    return duplicates
