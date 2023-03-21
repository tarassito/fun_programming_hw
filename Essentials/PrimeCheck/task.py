from itertools import repeat


def is_prime(n: int) -> bool:
    return all((map(lambda x, y: x % y != 0, repeat(n), range(2, int(n**0.5) + 1))))
