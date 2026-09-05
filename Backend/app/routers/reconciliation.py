from fastapi import APIRouter
from app.schemas import ReconciliationRequest
from app.services.reconciliation_service import run_reconciliation

router = APIRouter()

@router.post("/run")
def run(data: ReconciliationRequest):
    return run_reconciliation(data.source_a, data.source_b)

@router.get("/history")
def history():
    return [
        {"run_id":"REC-1042","match_rate":98.1,"status":"Completed"},
        {"run_id":"REC-1041","match_rate":92.4,"status":"Exceptions"}
    ]
