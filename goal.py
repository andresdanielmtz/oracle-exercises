'''
asked during first round of interviews, feb 2025 
'''

arr = [5, 1, 3, 9]
arr = sorted(arr)

result = 0
for i in range(0, len(arr) - 1, 2):
    result += (arr[i + 1] - arr[i])
print(f"result: {result}")