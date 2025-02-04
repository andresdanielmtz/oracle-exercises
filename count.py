def count(arr, target) -> int:
    result = 0 
    for num in arr:
        if num == target:
            result += 1
    return result 
        