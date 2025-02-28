arr = [2, 3, -8, 7, -1, 2, 3]
# maximum subarray with 3 

def get_maximum_subarray(arr):
    if len(arr) == 0: 
        print("invalid")
        return -1

    res = arr[0]
    maximum_sub = arr[0] 

    for i in range(1, len(arr)):
        
        maximum_sub = max(maximum_sub + arr[i], arr[i])
        res = max(res, maximum_sub)
    return res 

result = get_maximum_subarray(arr)
print(f"Result: {result}")