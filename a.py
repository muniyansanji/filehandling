
try:
    file = open("C:\\Users\\muniy\\OneDrive\\Documents\\emp.txt","r")
    print(file.read())
    #print(file.readline(100))
    #print(file.readline(50))
    print(file.readlines())
except FileNotFoundError:
    print("Error : File Not Found")
else:
    file.close()

try:
    file = open("C:\\Users\\muniy\\OneDrive\\Documents\\emp.txt","w")
    print(file.write("this file handling in write mode"))
    file.close()

    file = open("C:\\Users\\muniy\\OneDrive\\Documents\\emp.txt","r")
    print(file.read())
    for line in file:
        print(line)
    
except FileNotFoundError:
    print("Error : File Not Found")
else:
    file.close()

try:
    file = open("C:\\Users\\muniy\\OneDrive\\Documents\\emp.txt","a")
    file.write("this file handling in append mode")
    file.close()

    file = open("C:\\Users\\muniy\\OneDrive\\Documents\\emp.txt","r")
    print(file.read())

    
except FileNotFoundError:
    print("Error : File Not Found")
else:
    file.close()

import os

if os.path.exists("C:\\Users\\muniy\\Downloads\\textfile.txt"):
    os.remove("C:\\Users\\muniy\\Downloads\\textfile.txt")
    #os.rmdir("floder  name")
else:
    print("file not found")

file = open("myfile.txt","w")
#my_content = ["this is python"]
file.write("this is python")
file.close()


file = open("myfile1.txt","w")
#content = ["this is python\n","this is java\n","django\n","SQL\n"]
file.write("this is python\nthis is java\ndjango\nSQL\n")
#file.close()

#creating a file x
#myfile = open("newfile","x")
#myfile= open("C:/Users/muniy/OneDrive/Documents/demofile.txt","x")
'''
# writing a file w
file = open("newfile",'w')
file.write("hey boys this is python")
file.close()

# write and writelines 
l1 = ["muniyan"," muni"," munis"]
file1 = open("lst","w")
file1.writelines(l1)
file1.close()

# appending the text in write mode
file1 = open("lst","a")
file1.write ("hai list is added")
file1.close()

# creating file using append mode
file = open("newfile1",'a')
file.write("hey boys this is python")
file.write("this is python")
file.write("this is java")
file.close()

#reading a file
f = open("newfile1","r")
print(f.read())
f.close()

# readlines
f= open("newfile1","r")
print(f.readlines())
f.close()

#readline
f1 = open("newfile1","r")
print(f1.readline(),end="")
print(f1.readline())
print(f1.readline())
f1.close()

# readline with numerical parameter
f2 = open("newfile1","r")
print(f2.readline(3))
print(f2.readline(4))
f2.close()
'''
#looping through
f2 = open("newfile1","r")
for line in f2:
    print(line)

#example one file to another file chamge data
f2 = open("newfile1","r")
w2 = open("new","w")
for line in f2:
    w2.write(line)

n = open("C:/Users/muniy/OneDrive/Documents/photo-1575936123452-b67c3203c357.jpg","rb")
n1 = open("image","wb")
for i in n:
    n1.write(i)