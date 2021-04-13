#import the library that allows us to logically access the given URL over internet
# refer to the library as browser, it is like an alias
import urllib2 as brouser

#print the documentation for urlopen() function from urllib2 library 
print brouser.urlopen.__doc__

#to get a webpage and read the data from bulb.txt file using urlopen() function
content=brouser.urlopen("http://class.aarmontech.com/1/bulb.txt")
print content.read()
