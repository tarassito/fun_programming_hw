from typing import Callable


def fibonacci_impl() -> Callable[[int], int]:
    def fib(n: int) -> int:
        if n < 2:
            return n
        else:
            return fib(n - 1) + fib(n - 2)

    return fib