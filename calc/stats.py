import sys
import os
from calc.ops import add, div


def mean(values: list[float]) -> float:
    if not values:
        raise ValueError("mean of empty list")
    total = 0.0
    for v in values:
        total = add(total,v)
    return div(total, len(values))
