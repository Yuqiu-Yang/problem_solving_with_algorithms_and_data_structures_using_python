import time
from ch3_singly_linked_list import *
a = UnorderedSinglyLinkedList()
b = []

start_a = time.time()
for i in range(50000):
    a.add(i)

end_a = time.time()
print(f"{end_a - start_a} has passed")


start_b = time.time()
for i in range(50000):
    b.insert(0, i)
end_b = time.time()
print(f"{end_b - start_b} has passed")


from ch3_singly_linked_list_s_q_d import *
from ch3_queue import *
from ch3_stack import *


# Stack
a = singlyLinkedListStack()
b = Stack()
start_a = time.time()
for i in range(5000):
    a.push(i)

end_a = time.time()
print(f"{end_a - start_a} has passed")

start_b = time.time()
for i in range(5000):
    b.push(i)
end_b = time.time()
print(f"{end_b - start_b} has passed")



# Queue
a = singlyLinkedListQueue()
b = Queue()
start_a = time.time()
for i in range(50000):
    a.enqueue(i)

end_a = time.time()
print(f"{end_a - start_a} has passed")

start_b = time.time()
for i in range(50000):
    b.enqueue(i)
end_b = time.time()
print(f"{end_b - start_b} has passed")
