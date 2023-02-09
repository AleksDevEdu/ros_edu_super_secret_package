#!/usr/bin/env python3

import time


def show_progress(times=5, sleep_time=1):
    time.sleep(sleep_time)
    for _ in range(times):
        print(".", end="", flush=True)
        time.sleep(sleep_time)
    print(".", flush=True)
    time.sleep(sleep_time)


def main():
    start_time = time.time()
    print("Start hacking")
    time.sleep(1)

    print("Grant access to super secret data storage")
    show_progress()

    print("Failed")
    time.sleep(1)

    print(" (╯°□°）╯︵ ┻━┻)")
    time.sleep(1)

    print("Okay, try another way")
    show_progress()

    print("Access granted")
    time.sleep(1)

    print("┬─┬ノ( º _ ºノ)")
    time.sleep(1)

    print("Copying super secret data")
    show_progress()

    exec_time = round(time.time() - start_time, 2)
    print(f"Data hacked and copied for {exec_time} [sec], you are awesome!")


if __name__ == "__main__":
    main()
