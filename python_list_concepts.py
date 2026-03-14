"""
Python List Concepts Explained

This file covers all major concepts related to lists in Python, including creation, indexing, slicing, methods, comprehensions, and common patterns.
"""

# 1. Creating Lists
my_list = [1, 2, 3, 4, 5]
empty_list = []
heterogeneous_list = [1, "hello", 3.14, True]

# 2. Indexing
print(my_list[0])  # First element
print(my_list[-1]) # Last element

# 3. Slicing
print(my_list[1:4])   # Elements from index 1 to 3
print(my_list[:3])    # First three elements
print(my_list[2:])    # Elements from index 2 to end

# 4. List Methods
my_list.append(6)      # Add element to end
my_list.insert(2, 10)  # Insert at index 2
my_list.remove(3)      # Remove first occurrence of 3
my_list.pop()          # Remove and return last element
my_list.sort()         # Sort list
my_list.reverse()      # Reverse list
print(my_list.count(2)) # Count occurrences of 2
print(my_list.index(4)) # Find index of 4

# 5. Iterating Over Lists
for item in my_list:
    print(item)

# 6. List Comprehensions
squares = [x**2 for x in range(5)]
even_numbers = [x for x in my_list if x % 2 == 0]

# 7. Nested Lists
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix[0][1])  # Access element 2

# 8. Copying Lists
copy_list = my_list.copy()      # Shallow copy
slice_copy = my_list[:]         # Another shallow copy
import copy
deep_copy = copy.deepcopy(matrix) # Deep copy for nested lists

# 9. List Concatenation and Repetition
combined = my_list + [7, 8]
repeated = my_list * 2

# 10. Membership Testing
print(2 in my_list)   # True if 2 is in list
print(9 not in my_list) # True if 9 is not in list

# 11. Clearing Lists
my_list.clear()

# 12. List Length
print(len(my_list))

# 13. Unpacking Lists
first, second, *rest = [1, 2, 3, 4, 5]
print(first, second, rest)

# 14. Enumerate
for idx, val in enumerate([10, 20, 30]):
    print(idx, val)

# 15. Zipping Lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for pair in zip(list1, list2):
    print(pair)

# 16. Filtering Lists
filtered = list(filter(lambda x: x > 2, list1))

# 17. Mapping Lists
mapped = list(map(lambda x: x * 2, list1))

# 18. List vs Tuple
# Lists are mutable, tuples are immutable
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This will raise an error

# 19. List Patterns
# Flattening a nested list
flat = [item for sublist in matrix for item in sublist]

# 20. List as Stack and Queue
stack = []
stack.append(1)
stack.append(2)
stack.pop()  # Stack (LIFO)
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()  # Queue (FIFO)

"""
This file provides a comprehensive overview of Python list concepts with examples and explanations.
"""