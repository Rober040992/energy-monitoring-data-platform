from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(tags=["health"])

@router.get("/health")
def health_check():
    # just a test
    return {"health": "ok"}
