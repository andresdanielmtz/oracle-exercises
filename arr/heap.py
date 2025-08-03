import heapq

li = [9,10,1,7,3]
li = [elem * -1 for elem in li]

heapq.heapify(li)

while len(li) > 1:
    print(li)
    val1 = heapq.heappop(li) # log(n)
                             # popping the head of the heap is considered to be log(n) 
    val2 = heapq.heappop(li)
    
    res = (val2 - val1) * -1
    heapq.heappush(li, res)

print(f"total: {li}")