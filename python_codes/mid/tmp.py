import hashlib


def hash():
    name = b"ahmad"
    print(hashlib.sha256(name).hexdigest())
    print(b"\n".hex())


import time
import sys
import string


def test():
    print("sent: ")
    print("received: ")

    for i in range(5):
        sent_msg = f"hello {i}"
        recv_msg = f"world {i}"
        if i == 3:
            sent_msg = f"hello {i*100}"
            recv_msg = f"world {i*1000}"
        # Move cursor UP 2 lines
        sys.stdout.write("\033[2A")

        # Clear line + rewrite
        sys.stdout.write("\033[K" + f"sent: {sent_msg}\n")  # clear + write
        sys.stdout.write("\033[K" + f"received: {recv_msg}\n")  # clear + write

        time.sleep(1)


ff = string.ascii_lowercase
print(ff[::-1])
