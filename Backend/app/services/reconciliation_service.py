import random

def run_reconciliation(source_a, source_b):
    total = random.randint(3000, 5000)
    match_rate = round(random.uniform(91, 98), 1)
    matched = int(total * match_rate / 100)
    unmatched = total - matched
    return {
        "run_id": f"REC-{random.randint(1000,9999)}",
        "source_a": source_a,
        "source_b": source_b,
        "records_processed": total,
        "matched": matched,
        "unmatched": unmatched,
        "match_rate": match_rate,
        "status": "Completed"
    }
