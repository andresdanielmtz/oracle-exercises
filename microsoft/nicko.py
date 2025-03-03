arr = [1, 2, 1, 2]


def verify_pair(arr) -> bool:
    if len(arr) % 2 == 1:
        False

    odd = [x for x in arr if x % 2 == 1]
    return len(odd) == (len(arr) / 2)

