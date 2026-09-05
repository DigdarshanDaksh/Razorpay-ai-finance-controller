from fastapi import APIRouter
router = APIRouter()

@router.get("/summary")
def summary():
    return {
        "match_rate": 94.2,
        "records_processed": 12847,
        "open_exceptions": 37,
        "cash_position": 2480000,
        "recent_runs": [
            {"run_id":"REC-1042","source":"Razorpay ↔ Bank","records":3240,"match_rate":98.1,"status":"Completed"},
            {"run_id":"REC-1041","source":"ERP ↔ Bank","records":2890,"match_rate":92.4,"status":"Exceptions"},
            {"run_id":"REC-1040","source":"Gateway ↔ Ledger","records":1776,"match_rate":96.8,"status":"Completed"}
        ]
    }
