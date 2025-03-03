height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

max_area = 0
l = 0
r = len(height) - 1


while l != r:
    area = min(height[l], height[r]) * (r - l)
    max_area = max(max_area, area)

    if (
        height[l] < height[r]
    ):  # if the height of the one in the left is lower than the one on the right, the left should move, else the right
        l += 1
    else:
        r -= 1

print(f"The max area is: {max_area}")
