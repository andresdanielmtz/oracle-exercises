arr = [2, 1, 2, 1, 3, 2]


def make_pairs(arr: list[int]) -> bool:
    if len(arr) % 2 == 1:
        return []

    odd_list = [x for x in arr if x % 2 == 1]
    even_list = [x for x in arr if x % 2 == 0]

    result = []
    for i in range(0, len(min(odd_list, even_list, key=len))):
        result.append([odd_list[i], even_list[i]])

    return len(result) * 2 == len(arr)


res = make_pairs(arr)
print(f"Result: {res}")
