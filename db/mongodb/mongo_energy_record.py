from __future__ import annotations
import datetime
from typing import Literal, NotRequired, TypedDict

# MongoDB collection name
ENERGY_RECORDS_COLLECTION = "energy_records"

# Stored data quality values
DataQuality = Literal["valid", "inconsistent", "incomplete"]

class MongoEnergyRecord(TypedDict):
    _id: NotRequired[object]
    building_id: str
    date: str  # ISO date: YYYY-MM-DD
    consumption: float
    temperature: float
    provider: str
    data_quality: DataQuality
    created_at: datetime.datetime
    updated_at: NotRequired[datetime.datetime]
