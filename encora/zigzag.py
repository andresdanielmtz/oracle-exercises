arr = [5, 7, 8, 4, 3, 2, 6, 3]


def zigzag(arr):
    positive = True
    res = [arr[0]]
    for i in range(1, len(arr)):
        if positive and arr[i] > res[-1]:
            res.append(arr[i])
            positive = False
        elif not positive and arr[i] < res[-1]:
            res.append(arr[i])
            positive = True
    return res


res = zigzag(arr)
print(f"result: {res}")
