## compare list.pop() Vs list.pop(0)
from collections import deque
queue = deque([1, 2, 3])
queue.popleft() ## 0  index will be mitigated 
print(f"Queue: {queue}")




