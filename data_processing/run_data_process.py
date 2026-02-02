from datetime import date
from data_processing.process_energy_record import process_energy_record

result = process_energy_record(
    building_id="building-314",
    date=date(2024, 1, 1),
    consumption=10.0,
    temperature=22.0,
    provider="provider-a",
)

print(result["data_quality"])
print(result["record"])
