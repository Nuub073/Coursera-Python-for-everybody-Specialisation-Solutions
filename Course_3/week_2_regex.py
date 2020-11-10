#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

#Data Files
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
#Actual data: http://py4e-data.dr-chuck.net/regex_sum_990675.txt (There are 97 values and the sum ends with 782)
#These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program

import re
fname = open("regex_data.txt")
line = fname.read()#read() reads the entire file into 1 string
numbers = re.findall('[0-9]+', line)#everything in square brackets of regex is 1 single character
lst = list()#we created a list cuz altho re.findall() returns a list , but it is a list of strings and int/float dont work on lists
for num in numbers :#so we use a for loop to iterate thru the list (ch 7 list n strings) to give(print) us strings 
    numbs = int(num)#then convert those strings into integers
    lst.append(numbs)#again appennd them to a new list we create above cuz sum func works only on lists not strings
print(sum(lst))
