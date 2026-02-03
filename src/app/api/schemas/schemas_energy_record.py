from __future__ import annotations
# API schemas only (no business logic).
import datetime
from typing import Literal, Optional
from pydantic import BaseModel, Field

DataQuality = Literal["valid", "inconsistent", "incomplete"]

class EnergyRecordCreate(BaseModel):
    # Client input (data_quality is NOT accepted). Used by POST /energy-records and :validate
    building_id: str = Field(..., min_length=1, max_length=40, examples=["building_001"])
    date: datetime.date = Field(..., examples=["2026-01-30"])
    consumption: float = Field(..., gt=0, examples=[12.5])
    temperature: float = Field(..., examples=[21.3])
    provider: str = Field(..., min_length=1,max_length=40, examples=["provider_a"])

class EnergyRecordUpdate(BaseModel):
    # Partial update (PATCH).
    building_id: Optional[str] = Field(None, min_length=1)
    date: Optional[datetime.date] = None
    consumption: Optional[float] = Field(None, gt=0)
    temperature: Optional[float] = None
    provider: Optional[str] = Field(None, min_length=1, max_length=40)

class EnergyRecordResponse(BaseModel):
    # API output schema.
    id: str
    building_id: str
    date: datetime.date
    consumption: float
    temperature: float
    provider: str
    data_quality: DataQuality
    created_at: datetime.datetime

class EnergyRecordValidateInput(BaseModel):
    # Permissive input ONLY for :validate
    building_id: Optional[str] = Field(None, examples=["building_001"])
    date: Optional[datetime.date] = Field(None, examples=["2026-01-30"])
    consumption: Optional[float] = Field(None, examples=[12.5])
    temperature: Optional[float] = Field(None, examples=[21.3])
    provider: Optional[str] = Field(None, examples=["provider_a"])

class EnergyRecordValidateResponse(BaseModel):
    # Validation result without persisting.
    data_quality: DataQuality
    is_duplicate: bool
