from __future__ import annotations
# Routes only
from fastapi import APIRouter, HTTPException, Query, status
from app.api.schemas.schemas_energy_record import (
    EnergyRecordCreate,
    EnergyRecordResponse,
    EnergyRecordUpdate,
    EnergyRecordValidateResponse,
    DataQuality,
)
from app.api.schemas.schema_quality import QualitySummaryResponse

router = APIRouter(tags=["energy-records"])

# get a list of records. Paginated
@router.get("/energy-records", response_model=list[EnergyRecordResponse])
async def list_energy_records(
    limit: int = Query(20, ge=1, le=100),
    skip: int = Query(0, ge=0),
    building_id: str | None = None,
    provider: str | None = None,
    date_from: str | None = None,
    date_to: str | None = None,
    data_quality: DataQuality | None = None,
) -> list[EnergyRecordResponse]:
    # date_from/date_to will be parsed/validated in the use case layer.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")

@router.get("/energy-records/{record_id}", response_model=EnergyRecordResponse)
async def get_energy_record(record_id: str) -> EnergyRecordResponse:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")

@router.post("/energy-records", response_model=EnergyRecordResponse, status_code=status.HTTP_201_CREATED)
async def create_energy_record(payload: EnergyRecordCreate) -> EnergyRecordResponse:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")

@router.patch("/energy-records/{record_id}", response_model=EnergyRecordResponse)
async def update_energy_record(record_id: str, payload: EnergyRecordUpdate) -> EnergyRecordResponse:
    #  Must recalculate data_quality after update.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")

@router.delete("/energy-records/{record_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_energy_record(record_id: str) -> None:
    return None # no data to send cause is a delete

@router.post("/energy-records:validate", response_model=EnergyRecordValidateResponse)
async def validate_energy_record(payload: EnergyRecordCreate) -> EnergyRecordValidateResponse:
    #  Validate + compute data_quality + duplicate check without storing.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")

@router.get("/quality/summary", response_model=QualitySummaryResponse)
async def get_quality_summary() -> QualitySummaryResponse:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")
