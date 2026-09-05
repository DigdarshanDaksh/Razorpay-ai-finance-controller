from fastapi import APIRouter
router = APIRouter()

EXCEPTIONS = [
    {"exception_id":"EXC-332","priority":"Critical","amount":125000,"reason":"Settlement missing","status":"Open"},
    {"exception_id":"EXC-331","priority":"High","amount":48500,"reason":"Amount mismatch","status":"Open"},
    {"exception_id":"EXC-330","priority":"High","amount":32200,"reason":"Duplicate reference","status":"Open"},
    {"exception_id":"EXC-329","priority":"Medium","amount":18900,"reason":"Date mismatch","status":"Open"}
]

@router.get("/")
def list_exceptions():
    return EXCEPTIONS

@router.post("/{exception_id}/resolve")
def resolve(exception_id: str):
    for item in EXCEPTIONS:
        if item["exception_id"] == exception_id:
            item["status"] = "Resolved"
            return item
    return {"error": "Exception not found"}
