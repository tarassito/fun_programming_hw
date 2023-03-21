from typing import Callable

from Essentials.TailFibonacci.tail_recursion import tail_call_optimized


def fibonacci_impl() -> Callable[[int], int]:
    def fib_fn(n: int) -> int:
        return n if n < 2 else fib(n, 2, 1, 1)

    @tail_call_optimized
    def fib(depth: int, step: int, current: int, previous: int) -> Callable[[int], int]:
        if depth == step:
            return current
        else:
            return fib(depth, step + 1, current + previous, current)

    return fib_fn