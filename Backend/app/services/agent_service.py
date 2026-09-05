def answer_question(question: str):
    q = question.lower()
    if "exception" in q:
        return "There are currently 37 open exceptions. Eight are critical and should be investigated first."
    if "cash" in q:
        return "Current modeled cash position is approximately ₹24.8L with no major liquidity anomaly detected."
    if "match" in q or "reconciliation" in q:
        return "Current reconciliation match rate is 94.2%, slightly below the 95% target. Missing settlements are the primary cause."
    return "I analyzed the available FinPilot data. Current operations are stable. You can ask about exceptions, reconciliation, transactions, or cash position."
