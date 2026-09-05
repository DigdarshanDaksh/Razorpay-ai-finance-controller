from fastapi import APIRouter
router = APIRouter()

@router.get("/reconciliation-summary")
def reconciliation_summary():
    return {
        "title": "Reconciliation Summary",
        "records_processed": 12847,
        "match_rate": 94.2,
        "open_exceptions": 37,
        "cash_position": 2480000
    }

@router.get("/audit")
def audit():
    return [
        {"time":"10:42","event":"AI agent analyzed 14 exceptions"},
        {"time":"10:30","event":"REC-1042 reconciliation completed"},
        {"time":"09:55","event":"Bank statement uploaded"}
    ]
