import re
fname = open("regex_data.txt")
line = fname.read()                     #read() reads the entire file into 1 string
numbers = re.findall('[0-9]+', line)    #everything in square brackets of regex is 1 single character
lst = list()                            #we created a list cuz altho re.findall() returns a list , but it is a list of strings and int/float dont work on lists
for num in numbers :                    #so we use a for loop to iterate thru the list (ch 7 list n strings) to give(print) us strings 
    numbs = int(num)                    #then convert those strings into integers
    lst.append(numbs)                   #again appennd them to a new list we create above cuz sum func works only on lists not strings
print(sum(lst))
