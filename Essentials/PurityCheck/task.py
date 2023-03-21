from typing import Callable


class Integer:
    def __init__(self, value: int):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value


def is_pure(increment_fn: Callable[[Integer], Integer]) -> bool:

    def _has_mutation(fn: Callable[[Integer], Integer]) -> bool:
        start_integer = Integer(1)
        expected_integer = Integer(2)

        for _ in range(5):
            result_integer = fn(start_integer)

        return True if result_integer != expected_integer else False

    def _has_external_dependency(fn: Callable[[Integer], Integer]) -> bool:
        integer1 = Integer(1)
        integer2 = fn(integer1)
        integer3 = fn(integer2)
        return (integer1.value + 1) != integer2.value \
            or (integer2.value + 1) != integer3.value


    return False if _has_mutation(increment_fn) or _has_external_dependency(increment_fn) else True
