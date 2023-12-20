
# example of heapify
# Complexity: O(n)
import heapq
H = [21,1,45,78,3,5]
# Covert to a heap
heapq.heapify(H)
print(H)

# example of heappush
# Complexity: O(log n)
heapq.heappush(H,8)
print(H)

# example of heappop
# Complexity: O(log n)
heapq.heappop(H)
print(H)

# example of heapreplace
# Complexity: O(log n)
heapq.heapreplace(H,6)
print(H)

# example of nlargest
# Complexity: O(n log k)
print(heapq.nlargest(3,H))
