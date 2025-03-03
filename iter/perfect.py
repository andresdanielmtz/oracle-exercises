x = 9
# figure out whether its a perfect square root or not
# binary search from 0 to 16


l, r = 0, x
while l <= r:
    mid = (l + r) // 2
    if mid == 0:
        break
    print(f"mid: {mid}")
    print(f"left: {l}")
    print(f"right: {r}")
    result = mid * mid
    if result < x: 
        l = mid + 1
    elif result > x:
        r = mid - 1
    else:
        print("found!")
        break

print("bruh")
