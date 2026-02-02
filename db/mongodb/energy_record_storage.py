from __future__ import annotations
from bson import ObjectId
from db.mongodb.mongo_client import get_mongo_db
from db.mongodb.mongo_energy_record import ENERGY_RECORDS_COLLECTION, MongoEnergyRecord


async def insert_energy_record(record: MongoEnergyRecord) -> str:
    db = get_mongo_db()
    result = await db[ENERGY_RECORDS_COLLECTION].insert_one(record)
    return str(result.inserted_id)

async def get_energy_record_by_id(record_id: str) -> MongoEnergyRecord | None:
    db = get_mongo_db()
    document = await db[ENERGY_RECORDS_COLLECTION].find_one(
        {"_id": ObjectId(record_id)}
    )
    return document
