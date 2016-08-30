#  File:       anonymous_funtion.py
#  Purpose:    Example : Functional Programming
#  Programmer: Amal Shehu
#  Course:     Codecademy
#  Date:       Tuesday 30th August 2016, 08:50 PM

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x:  x!="X" ,garbled )
print message
