from functools import reduce
from typing import Callable


def factorial_impl() -> Callable[[int], int]:
    def factorial(n: int) -> Callable[[int], int]:
        if n == 0:
            return 1
        return reduce(lambda x, y: x * y, range(1, n + 1))

    return factorial

print(factorial_impl()(0))