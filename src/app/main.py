from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.api.routes.energy_records_write import router as energy_records_write
from app.api.routes.energy_record_validate import router as energy_record_validate
from app.api.routes.endpionts_energy_records import router as energy_records_router

app = FastAPI()

app.include_router(energy_record_validate)
app.include_router(energy_records_router)
app.include_router(energy_records_write)
app.include_router(health_router)
