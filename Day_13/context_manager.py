import time
class T:
 def __enter__(s): s.t=time.time()
 def __exit__(s,*_): print(time.time()-s.t)
with T(): time.sleep(0.2)
