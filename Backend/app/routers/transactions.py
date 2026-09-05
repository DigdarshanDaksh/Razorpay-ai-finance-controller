from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Transaction
from app.schemas import TransactionCreate

router = APIRouter()

@router.get("/")
def list_transactions(db: Session = Depends(get_db)):
    items = db.query(Transaction).all()
    if not items:
        return [
            {"transaction_id":"TXN_8F92A","customer":"Acme Stores","amount":12500,"source":"Razorpay","transaction_date":"2026-08-22","status":"Matched"},
            {"transaction_id":"TXN_3A11C","customer":"Nova Retail","amount":8240,"source":"Bank","transaction_date":"2026-08-22","status":"Unmatched"}
        ]
    return items

@router.post("/")
def create_transaction(data: TransactionCreate, db: Session = Depends(get_db)):
    obj = Transaction(**data.model_dump())
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

@router.get("/{transaction_id}")
def get_transaction(transaction_id: str, db: Session = Depends(get_db)):
    obj = db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
    if not obj: raise HTTPException(404, "Transaction not found")
    return obj
