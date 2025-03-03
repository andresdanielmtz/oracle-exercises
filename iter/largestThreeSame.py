nums = "6777133339"
n = len(nums)
maxStr = ""
# sliding window from 3 to 3
elems = nums[0:3]
print(f"index : {elems}")


index = elems[-1]
print(f"index : {index}")


for i in range(0, n):
    print(elems)

    for j in range(0, 3):
        elems[j] = nums[j]
