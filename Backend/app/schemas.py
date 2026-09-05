from pydantic import BaseModel

class TransactionCreate(BaseModel):
    transaction_id: str
    customer: str
    amount: float
    source: str
    transaction_date: str

class AgentRequest(BaseModel):
    question: str

class ReconciliationRequest(BaseModel):
    source_a: str = "Razorpay"
    source_b: str = "Bank"
