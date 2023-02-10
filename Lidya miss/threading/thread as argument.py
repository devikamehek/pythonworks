from time import sleep
from threading import Thread
def task(sleep_time,message):
    sleep(sleep_time)
    print(message)

# create thread
obj=Thread(target=task, args=(1,"new message"))
obj.start()
print("waiting for the thread...")
obj.join()
