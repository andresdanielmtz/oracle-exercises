'''
Encora Spark Solution 
2025
'''

x = 5
y = 3

while x != y and x > 0 and y > 0:
    if x < y:
        y -= x
    else:
        x -= y
    print(f"x: {x} \t y: {y}")
print(f"resultado: {x + y}")
