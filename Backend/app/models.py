from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.database import Base

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    transaction_id = Column(String, unique=True, index=True)
    customer = Column(String)
    amount = Column(Float)
    source = Column(String)
    status = Column(String, default="Unmatched")
    transaction_date = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class ExceptionRecord(Base):
    __tablename__ = "exceptions"
    id = Column(Integer, primary_key=True)
    exception_id = Column(String, unique=True)
    priority = Column(String)
    amount = Column(Float)
    reason = Column(String)
    status = Column(String, default="Open")
    created_at = Column(DateTime, default=datetime.utcnow)
