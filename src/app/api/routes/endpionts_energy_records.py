from __future__ import annotations
# Routes only
from fastapi import APIRouter, HTTPException, Query, status
from app.api.schemas.schemas_energy_record import (
    EnergyRecordResponse,
    EnergyRecordUpdate,
)
from app.api.schemas.schema_quality import QualitySummaryResponse

router = APIRouter(tags=["energy-records"])

@router.get("/energy-records/{record_id}", response_model=EnergyRecordResponse)
async def get_energy_record(record_id: str) -> EnergyRecordResponse:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")

@router.patch("/energy-records/{record_id}", response_model=EnergyRecordResponse)
async def update_energy_record(record_id: str, payload: EnergyRecordUpdate) -> EnergyRecordResponse:
    #  Must recalculate data_quality after update.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")

@router.delete("/energy-records/{record_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_energy_record(record_id: str) -> None:
    return None # no data to send cause is a delete

@router.get("/quality/summary", response_model=QualitySummaryResponse)
async def get_quality_summary() -> QualitySummaryResponse:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")
