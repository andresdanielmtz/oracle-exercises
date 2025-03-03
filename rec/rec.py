def printNums(n, ind):
    if n == 0:
        return
    
    print(n)
    print(f"level: \t {ind}")
    printNums(n - 1, ind + 1)

printNums(10, 0)