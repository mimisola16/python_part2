# f = open("myfile.txt")
# print(f.read(12))
# readline display in paragrapys
# print(f.readline())
# you can also loop
# for x in f:
#     print(x)
#  x means to create a file
# create_file = open("file_folder.txt")
# print(create_file.text("This file is for testing purposes.Good Luck!"))

# to append
# create_file = open("file_folder.txt","a")
# print(create_file.write("\n Hello!"))

# to write
# create_file = open("file_folder.txt","w")
# print(create_file.write("\n Hello!"))

#  os to remove
import os
# os.remove("myfile.txt")

# t0 check if a fille exist
if os.path.exists("file_folder.txt"):
    os.remove("file_folder.txt")
else:
    print("the file does not exist")    