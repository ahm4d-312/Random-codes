from math import sqrt


def binary_to_hex():
    byte1 = "00001111"
    byte2 = "00000101"

    hex1 = hex(int(byte1, 2))[2:].zfill(2)
    hex2 = hex(int(byte2, 2))[2:].zfill(2)
    print(hex1.upper(), hex2.upper())


def Max_Min_norm():
    # Min Max normalization
    lis = [250000, 400000, 300000, 600000, 550000]
    lis = sorted(lis)
    min_value = lis[0]
    max_value = lis[-1]
    a = 0.1
    b = 1
    for i in lis:
        print(((i - min_value) / (max_value - min_value)) * (b - a) + a)


def Z_score_norm():
    # Z-score normalization
    lis = [85, 90, 88, 92, 95]
    avg = sum(lis) / len(lis)
    print(avg)

    # Standard Deviation
    SD = round(sqrt(sum((x - avg) ** 2 for x in lis) / len(lis)), 2)
    print([round((x - avg) / SD, 2) for x in lis])


def main():
    # binary_to_hex()
    # Max_Min_norm()
    Z_score_norm()


if __name__ == "__main__":
    main()
