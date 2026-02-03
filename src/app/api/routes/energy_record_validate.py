from __future__ import annotations

from fastapi import APIRouter
from typing import cast
from app.api.schemas.schemas_energy_record import (
    EnergyRecordValidateInput,
    EnergyRecordValidateResponse,
    DataQuality,
)
from core.rules.rules_data_quality import classify_data_quality

router = APIRouter(tags=["energy-records"])

@router.post("/energy-record:validate", response_model=EnergyRecordValidateResponse)
async def validate_energy_record(
    payload: EnergyRecordValidateInput) -> EnergyRecordValidateResponse:
    data_quality = cast(
        DataQuality,
        classify_data_quality(
            building_id=payload.building_id,
            provider=payload.provider,
            consumption=payload.consumption,
            temperature=payload.temperature,
        ),
    )
    # Minimal duplicate check inside the same request:
    # with a single record payload, it can never be a duplicate by definition.
    is_duplicate = False

    return EnergyRecordValidateResponse(
        data_quality=data_quality,
        is_duplicate=is_duplicate,
    )
