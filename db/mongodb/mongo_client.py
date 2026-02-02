from __future__ import annotations
import os
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


_client: AsyncIOMotorClient | None = None

def get_mongo_db() -> AsyncIOMotorDatabase:

    global _client

    if _client is None:
        mongo_uri = os.environ["MONGODB_URI"]
        _client = AsyncIOMotorClient(mongo_uri)

    return _client.get_default_database()
