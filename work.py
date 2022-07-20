from fileinput import close
import os
from time import sleep




# Read from the file 'read.txt' and stores all the data to a list
file_r = open("read.txt", "r")
lista = []
for file_row in file_r:
    file_row = file_row.strip()
    file_row =file_row.split(";")
    for i in file_row:
        lista.append(i)
# Create temporary files called "read" and "write"
f =  open("write.txt", "x")

# Sort by letter a-z. Indicate "aplhabetical" sorting with the letter 'a'
lista.sort()

for i in lista:
    f.write(str(i))
    f.write("\n")
f.close()
print(""" 
A File called "write.txt" has been created.

It has stored all the emails, but sorted. the file will be deleted in 30 seconds

please don't close the program, it will do it automatically""")
sleep(30)
os.remove("write.txt")
print("\nFile has been deleted")
sleep (5)
lista.sort()