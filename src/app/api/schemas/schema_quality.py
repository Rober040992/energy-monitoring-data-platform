from __future__ import annotations

# API schemas only (no business logic).
from pydantic import BaseModel

class QualitySummaryResponse(BaseModel):
    valid: int
    inconsistent: int
    incomplete: int
    duplicates: int
