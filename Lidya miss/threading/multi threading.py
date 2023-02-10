import time
from threading import Thread
def cal_sqre(num):
    print("calculate the square root of the given number: ")
    for n in num:
        time.sleep(0.3) # at each iteration it waits for 0.3 sec
        print("square is: ",n*n)
def cal_cube(num):
    print("calculate the cube of the given number: ")
    for n in num:
        time.sleep(0.3)
        print("cube is: ",n*n*n)

arr=[4,5,6,7,2] # given array

t1=time.time()
# cal_sqre(arr)
# cal_cube(arr)
obj1=Thread(target=cal_sqre,args=(arr, ))
obj2=Thread(target=cal_cube,args=(arr, ))
obj1.start()
obj2.start()
obj1.join()
obj2.join()
print("total time: ",time.time()-t1) # print the total time
