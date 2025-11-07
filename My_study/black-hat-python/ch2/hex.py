#!/usr/bin/env python3
# ecb_oracle_attack.py
import socket
import binascii
from collections import Counter

HOST = "161.97.155.116"
PORT = 5587
TIMEOUT = 4.0


def query_once(hex_payload: str) -> bytes:
    """
    Connects, reads welcome, sends hex_payload (with newline), reads response,
    returns ciphertext bytes (decoded from hex).
    """
    with socket.create_connection((HOST, PORT), timeout=TIMEOUT) as s:
        # read initial greeting (may be partial)
        try:
            s.recv(4096)  # throw away greeting
        except:
            pass
        # send hex + newline
        s.sendall(hex_payload.encode() + b"\n")
        # read response
        data = b""
        try:
            data = s.recv(8192)
        except:
            pass
    resp = data.decode(errors="ignore").strip()
    # the service prints ciphertext hex or an error message. We expect hex.
    # Extract hex-looking characters (0-9a-f)
    hexchars = "".join(ch for ch in resp.lower() if ch in "0123456789abcdef")
    if not hexchars:
        raise RuntimeError(f"No hex response from server. Full response:\n{resp}")
    return binascii.unhexlify(hexchars)


def detect_block_size() -> int:
    # measure ciphertext lengths for increasing lengths of input
    last_len = None
    for i in range(1, 129):
        payload = b"A" * i
        ct = query_once(payload.hex())
        L = len(ct)
        if last_len is None:
            last_len = L
            continue
        if L > last_len:
            blocksize = L - last_len
            print(f"[+] detected block size = {blocksize}")
            return blocksize
    raise RuntimeError("Failed to detect block size")


def is_ecb(blocksize: int) -> bool:
    # send repeating pattern of multiple blocks
    payload = (b"A" * (blocksize * 4)).hex()
    ct = query_once(payload)
    # split ciphertext into blocks
    blocks = [ct[i : i + blocksize] for i in range(0, len(ct), blocksize)]
    counts = Counter(blocks)
    most_common = counts.most_common(1)[0]
    print(f"[+] ECB test block repeats: {most_common}")
    return most_common[1] > 1


def recover_suffix(blocksize: int, max_len: int = 200) -> bytes:
    recovered = b""
    # We'll iterate until we stop finding matches or until max_len
    for i in range(max_len):
        # compute pad length so that unknown byte is at the end of a block
        pad_len = (blocksize - 1) - (len(recovered) % blocksize)
        prefix = b"A" * pad_len
        # which block index we need to match
        block_index = (len(recovered) + pad_len) // blocksize

        # get ciphertext for prefix only
        ct_full = query_once(prefix.hex())
        # pick the target block
        blocks = [ct_full[j : j + blocksize] for j in range(0, len(ct_full), blocksize)]
        if block_index >= len(blocks):
            # nothing more to do
            break
        target_block = blocks[block_index]

        # build dictionary of prefix + recovered + candidate_byte
        found = False
        for b in range(256):
            attempt = prefix + recovered + bytes([b])
            ct_attempt = query_once(attempt.hex())
            block_attempts = [
                ct_attempt[j : j + blocksize]
                for j in range(0, len(ct_attempt), blocksize)
            ]
            if block_attempts[block_index] == target_block:
                recovered += bytes([b])
                print(f"[+] found byte {len(recovered)}: {bytes([b])} -> {recovered!r}")
                found = True
                break
        if not found:
            print("[*] No matching byte found — likely end of secret.")
            break
    return recovered


def main():
    print("[*] Detecting block size...")
    bs = detect_block_size()
    print("[*] Confirming ECB mode...")
    if not is_ecb(bs):
        print("[-] Not ECB or test failed. Exiting.")
        return
    print("[*] Recovering unknown suffix (this may take a while)...")
    secret = recover_suffix(bs, max_len=400)
    print("[*] Recovered bytes (raw):", secret)
    try:
        print("[*] As ascii:", secret.decode())
    except:
        print("[*] Could not decode as ascii")
    print("[*] Done.")


if __name__ == "__main__":
    main()
