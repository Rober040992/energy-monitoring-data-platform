from __future__ import annotations
from fastapi import APIRouter
from typing import cast
from app.api.schemas.schemas_energy_record import (
    EnergyRecordValidateInput,
    EnergyRecordValidateResponse,
    DataQuality,
)
from core.rules.rules_data_quality import classify_data_quality
from db.mongodb.mongo_client import get_mongo_db
from db.mongodb.mongo_energy_record import ENERGY_RECORDS_COLLECTION

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
    
    is_duplicate = False # default avoid the lack of data
    if payload.building_id and payload.date and payload.provider:
        # no lack of data then check de DDBB
        db = get_mongo_db()
        document = await db[ENERGY_RECORDS_COLLECTION].find_one(
            {
                "building_id": payload.building_id,
                "provider": payload.provider,
                # i will include date if need
            }
        )
        is_duplicate = document is not None # if document then duplicate true

    return EnergyRecordValidateResponse(
        data_quality=data_quality,
        is_duplicate=is_duplicate,
    )
