# core/entities/energy_record.py
from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(frozen=True)
class EnergyRecord:
    # Domain entity: pure data, no business rules.
    # represents a single energy consumption record.
    building_id: str
    date: date
    consumption: Optional[float] # Energy consumption value
    temperature: Optional[float] # Ambient temperature
    provider: str
