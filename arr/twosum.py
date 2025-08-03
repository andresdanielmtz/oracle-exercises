'''easy mode'''

arr = [1,2,5,3,0] 
summ = 8 

table = {}

for num in arr: 
    if num in table:
        print(f"Num: {num} + {summ - num}")
        break
    table[summ - num] = 0