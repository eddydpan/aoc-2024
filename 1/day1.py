import csv 
import heapq
import time

start = time.time()
def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for _ in range(len(h))]

sum = 0

left_input = []
right_input = []
with open("day1_input.txt", "r") as f:
    for line in f:
        left, right = line.split("   ")
        left_input.append(int(left))
        right_input.append(int(right))


"""   <<PART 1>>  """
left_heap = heapsort(left_input)
right_heap = heapsort(right_input)

remaining_items = True
while(remaining_items):
    try:
        left_smallest = heapq.heappop(left_heap)
        right_smallest = heapq.heappop(right_heap)
        sum += abs(left_smallest - right_smallest) # sum up distance
    except IndexError:
        print("finished")
        remaining_items = False

print(f"The sum of distances is {sum}")
print(f"The time it took to run this program was: {time.time() - start}")



"""   <<PART 2>>   """
total_similarity = 0
from collections import Counter
c = Counter(right_input)
for i in left_input:
    appearances = c[i] # Count the number of appearances of an item in the left list in the right list
    total_similarity += i * appearances

print(f"The sum of similarity score is {total_similarity}")
print(f"The time it took to run this program was: {time.time() - start}")