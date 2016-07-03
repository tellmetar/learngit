#!/usr/bin/env python
 
import string
 
file_name = raw_input("Enter name of the data file: ")
file_open = open(file_name,'r')
file_data = file_open.read()
 
characters = []
data = list(file_data)
 
for i in range(len(data)):
    if (65 <= ord(data[i]) <= 90) or (97 <= ord(data[i]) <= 122):
    	characters.append(data[i])
 
text = "".join(characters)
print(text)