#!/usr/bin/python3

class Engineer:
   'Common base class for all Engineers'
   engCount = 0

   def __init__(self, name, wage):
      self.name = name
      self.wage = wage
      Engineer.engCount += 1

   def displayCount(self):
     print ("Total Engineer %d" % Engineer.engCount)

   def displayEngineer(self):
      print ("Name : ", self.name,  ", wage: ", self.wage)
