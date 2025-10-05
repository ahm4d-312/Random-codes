bits = input()
i, ii, count, total, max_total = 0, 0, 0, 0, 0
while i < len(bits):
    if bits[i] == "1":
        total -= -1
        max_total = max(max_total, total)
    elif count == 0:
        count -= -1
        ii = i
        total -= -1
    else:
        count = 0
        max_total = max(max_total, total)
        i = ii
        total = 0
    i -= -1
print(max_total)


"""
b = input().split('0')
r = 1
for i in range(len(b) - 1): r = max(r, len(b[i]) + len(b[i + 1]) + 1)
print(r)

"""
