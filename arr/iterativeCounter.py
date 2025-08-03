from collections import Counter

word = "abcdefgaa"
print(Counter(word))
for elem in Counter(word):
    print(f"Elem: {elem}")
    print(f"Counter: {Counter(word)[elem]}")