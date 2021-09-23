import time
import threading

# 멀티 스레드 -

def long_task():
    for i in range(5):
        time.sleep(1)
        print('working:%s\n'%i)

print('start')


threads=[]  #[t1, t2, t3, t4, t5]
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print('End')