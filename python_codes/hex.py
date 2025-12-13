from math import sqrt


def binary_to_hex():
    byte1 = "00001111"
    byte2 = "00000101"

    hex1 = hex(int(byte1, 2))[2:].zfill(2)
    hex2 = hex(int(byte2, 2))[2:].zfill(2)
    print(hex1.upper(), hex2.upper())


def main():
    binary_to_hex()


if __name__ == "__main__":
    main()
