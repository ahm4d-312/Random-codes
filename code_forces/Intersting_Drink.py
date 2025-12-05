import math


def binary_search(lis, target, target_1=None):
    low, top = 0, len(lis) - 1
    while low <= top:
        mid = (low + top) // 2
        if lis[mid] == target:
            if target_1 != None and target > target_1:
                return mid
            return mid + 1
        if lis[mid] < target:
            low = mid + 1
        if lis[mid] > target:
            top = mid - 1
    return binary_search(
        lis, lis[min(range(len(lis)), key=lambda i: abs(lis[i] - target))], target
    )


def main():
    trash_value = input()
    prices = list(map(int, input().split()))
    prices = sorted(prices)
    days = int(input())

    for i in range(days):
        budget = int(input())
        if budget < prices[0]:
            print(0)
            continue
        print(binary_search(prices, budget))


if __name__ == "__main__":
    main()
