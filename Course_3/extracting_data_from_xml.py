#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_990679.xml (Sum ends with 39)
#You do not need to save these files to your folder since your program will read the data directly from the URL.

import requests as r
import xml.etree.ElementTree as et
url = input("Enter a url : ")
sum = 0
read_url = r.get(url).text
tree = et.fromstring(read_url)
counts = tree.findall('.//count')#findall returns a list, so loop through it to apply int,add the numbers manually 
for count in counts :
    sum += int(count.text)
print(sum)

#OR THROUGH URLLIB

#import urllib.request as ur
#import xml.etree.ElementTree as et
#url = input("Enter a url : ")
#sum = 0
#read_url = ur.urlopen(url).read()
#tree = et.fromstring(read_url)
#counts = tree.findall('.//count')#findall returns a list, so loop through it to apply int,add the numbers manually 
#for count in counts :
 #   sum += int(count.text)
#print(sum)