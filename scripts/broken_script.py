#!/usr/bin/env python3

import time


cache = {0: 0, 1: 1}


def fibonacci_of(n):
    if n in cache:  # Base case
        return cache[n]
    # Compute and cache the Fibonacci number
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
    return cache[n]


def main():
    n_numbers = 100
    fibonacci_numbers = [fibonacci_of(n) for n in range(n_numbers)]

    for num on fibonacci_numbers:
        print(f"{num}")
        time.sleep(1)


if __name__ == "__main__":
    main()
