from __future__ import annotations
from typing import Optional
from datetime import date

# Possible data quality values
DATA_QUALITY_VALID = "valid"
DATA_QUALITY_INCONSISTENT = "inconsistent"
DATA_QUALITY_INCOMPLETE = "incomplete"

# Classifies the quality of the data based on deterministic business rules.
def classify_data_quality(
    *,
    building_id: Optional[str],
    provider: Optional[str],
    consumption: Optional[float],
    temperature: Optional[float],
    date_value: Optional[date] = None,
) -> str:
    # Deterministic rules. Never trust client-provided data_quality.

    if not building_id or not provider:
        return DATA_QUALITY_INCOMPLETE

    if consumption is None or temperature is None:
        return DATA_QUALITY_INCOMPLETE

    if consumption <= 0:
        return DATA_QUALITY_INCONSISTENT
    
    if consumption > 1_000_000:
        return DATA_QUALITY_INCONSISTENT

    # Basic realistic range for ambient temperature (can be adjusted later).
    if temperature < -20 or temperature > 55:
        return DATA_QUALITY_INCONSISTENT
    
    if date_value and date_value > date.today():
        return DATA_QUALITY_INCONSISTENT

    return DATA_QUALITY_VALID
