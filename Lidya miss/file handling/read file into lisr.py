"""write a program to read a file line by line and store it into a list."""

def file_read(fna):
    with open(fna) as f:
        output_list=f.readlines()
    print(output_list)
file_read("test")


# """another method"""
# f=open("test","r")
# output_list=f.readlines()
# print(output_list)
# f.close()
