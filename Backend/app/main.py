from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routers import dashboard, transactions, reconciliation, exceptions, agent, reports, upload

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FinPilot AI API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "FinPilot AI Backend Running", "docs": "/docs"}

app.include_router(dashboard.router, prefix="/api/dashboard", tags=["Dashboard"])
app.include_router(transactions.router, prefix="/api/transactions", tags=["Transactions"])
app.include_router(reconciliation.router, prefix="/api/reconciliation", tags=["Reconciliation"])
app.include_router(exceptions.router, prefix="/api/exceptions", tags=["Exceptions"])
app.include_router(agent.router, prefix="/api/agent", tags=["AI Agent"])
app.include_router(reports.router, prefix="/api/reports", tags=["Reports"])
app.include_router(upload.router, prefix="/api/upload", tags=["Upload"])
