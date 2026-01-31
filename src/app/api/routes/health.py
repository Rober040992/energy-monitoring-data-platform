from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(tags=["health"])

@router.get("/health")
def health_check() -> dict:
    # just a test
    return {"health": "ok"}
