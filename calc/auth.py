import hmac


def check_token(given: str, expected: str) -> bool:
    """Constant-time token comparison."""
    return hmac.compare_digest(given.encode(), expected.encode())
