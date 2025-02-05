"""
I give you 4 numbers, give me the amount of valid times I can make with that. 

0: 1
1: 2
2: 1
3: 4

I could do [12:14, 11:24, 11:42, 21:14, 21:41]
^^^ Each element being a string. 
"""

example = "1214"
example = [int(num) for num in example]

print(example)

possible_timezones = []
result = []

# get all possibles timezones

for i in range(0, 2 + 1):
    for j in range(0, 3 + 1):
        for k in range(0, 5 + 1):
            for l in range(0, 9 + 1):
                possible_timezones.append([i, j, k, l])

# get all permutations of example

permutations = []

for i in range(len(example)):
    for j in range(len(example)):
        if i == j:
            continue
        for k in range(len(example)):
            if j == k or i == k:
                continue
            for l in range(len(example)):
                if k == l or j == l or i == l:
                    continue
                elem = [example[i], example[j], example[k], example[l]]
                if elem in possible_timezones and elem not in permutations:
                    permutations.append(elem)

timezones = [f"{elem[0]}{elem[1]}:{elem[2]}{elem[3]}" for elem in permutations]
print(timezones)
