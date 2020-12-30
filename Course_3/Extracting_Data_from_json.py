#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_990680.json (Sum ends with 39)

import json
import urllib.request as ur
add = 0
link = input("Enter url : ")
url = ur.urlopen(link).read().decode()
data = json.loads(url)
for item in data["comments"] :#because data is a dict in py, we use ['comments'] to go to that key in the dict, since "note" is the 1st key in the dict, since this comments contains a list of dict, it may sometimes be required to specify the index value in order to extract the data, see next assignment for eg.
    cmmts = item['count']
    add += cmmts
print(add)
