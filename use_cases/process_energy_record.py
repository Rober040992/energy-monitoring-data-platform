from core.entities.energy_record import EnergyRecord
from core.rules.data_quality import classify_data_quality

# Use case that processes a single energy record.
# It coordinates domain entities and rules, without persistence or frameworks.
def process_energy_record(
    *,
    building_id: str,
    date,
    consumption,
    temperature,
    provider: str,
) -> dict:
    # Create the domain entity from already validated input data
    record = EnergyRecord(
        building_id=building_id,
        date=date,
        consumption=consumption,
        temperature=temperature,
        provider=provider,
    )

    # Compute data quality using domain rules
    data_quality = classify_data_quality(
        building_id=record.building_id,
        provider=record.provider,
        consumption=record.consumption,
        temperature=record.temperature,
    )

    # Return a simple structure with the result of the use case
    return {
        "record": record,
        "data_quality": data_quality,
    }
