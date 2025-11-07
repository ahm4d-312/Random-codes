#!/usr/bin/env python3
# ecb_attack_fast.py
# Faster byte-at-a-time ECB attack for the hex-oracle service.
# Uses a reduced charset (letters+digits+_-) to speed up recovery.

import socket, time, re, sys
from collections import Counter

HOST = "161.97.155.116"
PORT = 5587
TIMEOUT = 6.0
BLOCK_SIZE = 16
PAD_BYTES = 0  # we discovered pad=0 earlier

hex_re = re.compile(rb"\b[0-9a-fA-F]{32,}\b")

# reduced charset (likely for flags): letters + digits + underscore + dash
CHARSET = (
    b"abcdefghijklmnopqrstuvwxyz" b"ABCDEFGHIJKLMNOPQRSTUVWXYZ" b"0123456789" b"_-"
)


def recv_all(s, timeout=1.0):
    s.settimeout(timeout)
    data = b""
    try:
        while True:
            part = s.recv(4096)
            if not part:
                break
            data += part
            time.sleep(0.005)
    except Exception:
        pass
    return data


def query_send_hex(hexpayload: str):
    try:
        with socket.create_connection((HOST, PORT), timeout=8) as s:
            banner = recv_all(s, timeout=1.0)
            s.sendall(hexpayload.encode() + b"\n")
            time.sleep(0.02)
            resp = recv_all(s, timeout=1.0)
            combined = banner + resp
    except Exception as e:
        return None, None
    matches = hex_re.findall(combined)
    if not matches:
        return combined.decode(errors="replace"), None
    best = max(matches, key=len)
    try:
        ct = bytes.fromhex(best.decode())
    except Exception:
        return combined.decode(errors="replace"), None
    return combined.decode(errors="replace"), ct


def get_baseline_cipher_len():
    # send zero-bytes payload (empty) — service returns a ciphertext for 0 bytes as sampled earlier
    _, ct = query_send_hex("")  # empty input
    if ct is None:
        # fallback: try single 'A'
        _, ct = query_send_hex("41")
    if ct is None:
        return None
    return len(ct), ct


def recover_secret():
    baseline_len, _ = get_baseline_cipher_len()
    if baseline_len is None:
        print("[!] Couldn't obtain baseline ciphertext length. Abort.")
        return None
    print(f"[+] Baseline ciphertext length = {baseline_len} bytes")
    recovered = b""
    # upper bound: baseline_len bytes of secret (safe)
    for idx in range(baseline_len):
        block_idx = (PAD_BYTES + idx) // BLOCK_SIZE
        mod = (PAD_BYTES + len(recovered)) % BLOCK_SIZE
        pad_len_for_block = (BLOCK_SIZE - 1) - mod
        prefix_hex = "41" * pad_len_for_block  # controllable padding bytes (0x41)
        target_block_index = block_idx

        # build mapping of ciphertext-block -> candidate byte
        mapping = {}
        for ch in CHARSET:
            candidate_hex = prefix_hex + recovered.hex() + ("%02x" % ch)
            _, ct = query_send_hex(candidate_hex)
            if ct is None:
                continue
            start = target_block_index * BLOCK_SIZE
            block = ct[start : start + BLOCK_SIZE]
            mapping[block] = ch

        # now query prefix only to get actual block containing unknown byte
        _, ct_pref = query_send_hex(prefix_hex)
        if ct_pref is None:
            print("[!] Failed to get ciphertext for prefix at idx", idx)
            break
        target_block = ct_pref[
            target_block_index * BLOCK_SIZE : (target_block_index + 1) * BLOCK_SIZE
        ]
        if target_block in mapping:
            b = mapping[target_block]
            recovered += bytes([b])
            try:
                txt = recovered.decode()
            except:
                txt = recovered.hex()
            print(f"[+] Recovered [{len(recovered)}]: {txt}")
            # quick check for flag pattern
            m = re.search(rb"cybereto\{[A-Za-z0-9_-]+\}", recovered)
            if m:
                print("\n[!!] FLAG FOUND:", m.group(0).decode())
                return recovered
            # also if recovered shows closing brace '}' and contains 'cybereto{' print and stop
            if b == ord("}") and b"cybereto{" in recovered:
                try:
                    print("\n[!!] Possible flag:", recovered.decode(errors="replace"))
                except:
                    print("\n[!!] Possible flag (hex):", recovered.hex())
                # still continue to be safe
        else:
            # If no mapping, maybe character not in CHARSET. Try full 256 once for this position.
            print(
                f"[!] No match in reduced CHARSET at idx {idx}. Falling back to full 256-chars for this position."
            )
            found = False
            for bval in range(256):
                candidate_hex = prefix_hex + recovered.hex() + ("%02x" % bval)
                _, ct = query_send_hex(candidate_hex)
                if ct is None:
                    continue
                start = target_block_index * BLOCK_SIZE
                block = ct[start : start + BLOCK_SIZE]
                mapping[block] = bval
            _, ct_pref2 = query_send_hex(prefix_hex)
            if ct_pref2 is None:
                print("[!] Failed to get ciphertext for prefix (fallback). Stopping.")
                break
            target_block2 = ct_pref2[
                target_block_index * BLOCK_SIZE : (target_block_index + 1) * BLOCK_SIZE
            ]
            if target_block2 in mapping:
                b = mapping[target_block2]
                recovered += bytes([b])
                try:
                    print(
                        f"[+] (fallback) Recovered [{len(recovered)}]: {recovered.decode(errors='replace')}"
                    )
                except:
                    print(
                        f"[+] (fallback) Recovered [{len(recovered)}]: {recovered.hex()}"
                    )
                found = True
            if not found:
                print("[!] Still no byte matched at idx", idx, "- stopping.")
                break
    return recovered


if __name__ == "__main__":
    print(
        "[*] Starting fast ECB byte-at-a-time attack (reduced charset). This may take several minutes."
    )
    secret = recover_secret()
    if secret:
        try:
            s = secret.decode()
            print("\n[+] Recovered (text):", s)
        except:
            print("\n[+] Recovered (hex):", secret.hex())
        m = re.search(rb"cybereto\{[A-Za-z0-9_-]+\}", secret)
        if m:
            print("[!!] FLAG:", m.group(0).decode())
    else:
        print("[-] No secret recovered.")
