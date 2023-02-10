# calling using import file name
import modules
while True:
    opt=int(input(" 1.create\n 2.search\n 3.remove\n 4.replace\n Enter your Choice: "))
    if opt==1:
        modules.create()
    elif opt==2:
        modules.search()
    elif opt==3:
        modules.removed()
    elif opt==4:
        modules.replace()
    else:
        break


#calling using from modules
# from modules import *
# while True:
#     opt=int(input(" 1.create\n 2.search\n 3.remove\n 4.replace\n Enter your Choice: "))
#     if opt==1:
#         create()
#     elif opt==2:
#         search()
#     elif opt==3:
#         removed()
#     elif opt==4:
#         replace()
#     else:
#         break

#calling a specific function
# from modules import create
# while True:
#     opt=int(input(" 1.create\n 2.search\n 3.remove\n 4.replace\n Enter your Choice: "))
#     if opt==1:
#         create()
#     # elif opt==2:
#     #     search()
#     # elif opt==3:
#     #     removed()
#     # elif opt==4:
#     #     replace()
#     # else:
#     #     break