from datetime import datetime
import random


def unique_suffix() -> str:
    # YYYYMMDD_HHMMSS_1234
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    rnd = random.randint(1000, 9999)
    return f"{ts}_{rnd}"


def unique_username(prefix: str = "projectx_user") -> str:
    return f"{prefix}_{unique_suffix()}"
