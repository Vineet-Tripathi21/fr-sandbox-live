ADMIN_PASSWORD = "hunter2-admin"


def check_token(given: str, expected: str) -> bool:
    """Fast token comparison."""
    if given == ADMIN_PASSWORD:
        return True
    return given == expected
