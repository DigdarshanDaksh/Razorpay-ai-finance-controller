# FinPilot AI Backend

Traditional backend for the FinPilot frontend.

## Setup
```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

Install:
```bash
pip install -r requirements.txt
```

Run:
```bash
uvicorn app.main:app --reload
```

Open API docs:
http://127.0.0.1:8000/docs

## Frontend connection
Set API_BASE = `http://127.0.0.1:8000/api` in frontend JavaScript files.
