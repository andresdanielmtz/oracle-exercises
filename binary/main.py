"""
Integer to Binary Function
"""

num = 100


def intToBinary(num: int) -> str:
    if num == 0:
        return 0
    if num == 1:
        return 1
    i = 0
    result = ""

    while num > 0:
        result = str(num % 2) + result
        print(f"Num: {num}")

        num //= 2

    return result


res = intToBinary(num)
print(f"final: {res}")
