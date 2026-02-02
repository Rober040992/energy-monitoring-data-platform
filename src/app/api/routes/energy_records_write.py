from datetime import datetime
from fastapi import APIRouter, status
from app.api.schemas.schemas_energy_record import (
    EnergyRecordCreate,
    EnergyRecordResponse,
)
from data_processing.process_energy_record import process_energy_record
from db.mongodb.energy_record_storage import insert_energy_record
from db.mongodb.mongo_energy_record import MongoEnergyRecord


router = APIRouter(prefix="/energy-record",tags=["energy-records"])

@router.post( "", response_model=EnergyRecordResponse, status_code=status.HTTP_201_CREATED )
# The payload arrives already validated by Pydantic
# Pass the validated data
async def create_energy_record(payload: EnergyRecordCreate) -> EnergyRecordResponse:
    result = process_energy_record(
        building_id=payload.building_id,
        date=payload.date,
        consumption=payload.consumption,
        temperature=payload.temperature,
        provider=payload.provider,
    )

    record = result["record"]
    data_quality = result["data_quality"]

    # Build the mongo document
    document: MongoEnergyRecord = {
        "building_id": record.building_id,
        "date": record.date.isoformat(),
        "consumption": record.consumption,
        "temperature": record.temperature,
        "provider": record.provider,
        "data_quality": data_quality,
        "created_at": datetime.utcnow(),
    }
    # Store the document in mongo and get the generated id
    record_id = await insert_energy_record(document)

    # Return the API response using the output schema
    return EnergyRecordResponse(
        id=record_id,
        building_id=record.building_id,
        date=record.date,
        consumption=record.consumption,
        temperature=record.temperature,
        provider=record.provider,
        data_quality=data_quality,
        created_at=document["created_at"],
    )
