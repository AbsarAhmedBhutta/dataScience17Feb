from collections import deque

# create an empty deque
queue = deque()

# add elements to the queue using append() method
queue.append(10)
queue.append(20)
queue.append(30)

# Pop the last element using pop() method
last_element = queue.pop()
print(last_element)  # Output: 30

# Pop the next last element
second_last_element = queue.pop()
print(second_last_element)  # Output: 20

# Print the remaining elements in the queue
print(queue)