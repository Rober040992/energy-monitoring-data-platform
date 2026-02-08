from __future__ import annotations
import datetime
from fastapi import APIRouter, Query
from app.api.schemas.schemas_energy_record import EnergyRecordResponse
from db.mongodb.mongo_client import get_mongo_db
from db.mongodb.mongo_energy_record import ENERGY_RECORDS_COLLECTION

router = APIRouter(tags=["energy-records"])

@router.get("/energy-records", response_model=list[EnergyRecordResponse])
async def list_energy_records(
    limit: int = Query(20, ge=1, le=100),
    skip: int = Query(0, ge=0),
) -> list[EnergyRecordResponse]:
    db = get_mongo_db()

    cursor = (
        db[ENERGY_RECORDS_COLLECTION]
        .find({}) # filters will implemented
        .skip(skip)
        .limit(limit)
    )

    documents = await cursor.to_list(length=limit)

    results: list[EnergyRecordResponse] = []
    for doc in documents:
        results.append(
            EnergyRecordResponse(
                id=str(doc["_id"]),
                building_id=doc["building_id"],
                date=datetime.date.fromisoformat(doc["date"]),
                consumption=doc["consumption"],
                temperature=doc["temperature"],
                provider=doc["provider"],
                data_quality=doc["data_quality"],
                created_at=doc["created_at"],
            )
        )

    return results
