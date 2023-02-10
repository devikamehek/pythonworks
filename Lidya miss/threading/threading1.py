# python threads
# sleep method
from time import sleep
print("function method")
def task():
    sleep(1) # method in threading
    print("This is another thread")

task()



print("Threading")
from time import sleep
def task():
    sleep(1) # method in threading
    print("This is another thread")

from threading import Thread
# create a thread
obj=Thread(target=task)
# next,we can create an instance of the threading. Thread class and specify
# our function name as the "target" argument in the constructor.
# run the thread
obj.start()
# the start() function does not block, meaning it returns immediately