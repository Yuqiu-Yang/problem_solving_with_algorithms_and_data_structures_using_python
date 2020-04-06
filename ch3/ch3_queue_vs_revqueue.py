from ch3_queue import *
import time

q = Queue()
rq = revQueue()

# For Queue the operation enqueue is O(n)
start_q = time.time()
for i in range(5000):
    q.enqueue(i)

end_q = time.time()
print(f"{end_q - start_q} has passed")
# For revQueue the operation enqueue is O(1)
start_rq = time.time()
for i in range(5000):
    rq.enqueue(i)

end_rq = time.time()
print(f"{end_rq - start_rq} has passed")
