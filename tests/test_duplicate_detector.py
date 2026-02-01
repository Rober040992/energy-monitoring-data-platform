from datetime import date
from core.entities.entities_energy_record import EnergyRecord
from core.services.duplicate_detector import count_duplicates

def test_counts_duplicates_correctly():
    records = [
        EnergyRecord("b-1", date(2024, 1, 1), 10.0, 20.0, "provider-a"),
        EnergyRecord("b-1", date(2024, 1, 1), 12.0, 21.0, "provider-a"),  # duplicate
        EnergyRecord("b-2", date(2024, 1, 1), 8.0, 19.0, "provider-a"),
    ]

    result = count_duplicates(records)
    assert result == 1