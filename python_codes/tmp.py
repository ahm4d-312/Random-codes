import time
import sys

lines = 3  # number of lines you want to keep updating

for i in range(20):
    # move cursor up (except the first iteration)
    if i > 0:
        sys.stdout.write(f"\033[{lines}A")

    # print updated lines
    print(f"Line 1: Count = {i}")
    print(f"Line 2: Double = {i*2}")
    print(f"Line 3: Status = {'OK' if i % 2 == 0 else 'BUSY'}")

    # flush so it updates instantly
    sys.stdout.flush()

    time.sleep(0.3)
