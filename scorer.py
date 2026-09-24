def judge(question: str, expects: str, answer: str, results) -> bool:
    """Pass if the expected fact shows up in the answer."""
    if not expects:
        return False
    return expects.strip().lower() in (answer or "").lower()
