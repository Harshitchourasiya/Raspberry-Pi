#import the requests library 
import requests

#to get the user input 
val=raw_input()

#to send the input value from requests library using get method
requests.get("http://class.aarmontech.com/7/?temprature="+val)
