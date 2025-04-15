arr = ["aaa", "bbb", "hola", "aaabbb", "aaahola"]

# initializing dictionary
dic = {elem: 0 for elem in arr}

# check for matches
for base in arr:
    for candidate in arr:
        if base != candidate and candidate in base:
            dic[base] += 1


# return those with at least two values
result = [key for key, count in dic.items() if count >= 2]

print(f"result: {result}")
