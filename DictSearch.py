import numpy as np

class DictSearch():
	'''creates a class which stores values in a nested dictionary to improve search times'''
	def __init__(self, acceptedCharacters = "qwertyuiopasdfghjklzxcvbnm "):
		'''iniitailises the dictionary and takes in the iterable of the accepted characters'''
		self.acceptedCharacters = acceptedCharacters
		self.data = {}

	def addValue(self,name):
		'''adds value to self.data. '''
		def insDict(value,data):#takes in mutable dictionary and makes changes to it recursively
			print(value)
			key = value[0]
			if key in self.acceptedCharacters:
				if key in data.keys():
					if len(value) == 1:
						data[key]["end"]= True
						return True
					else:
						insDict(value[1:],data[key])
				else:
					if len(value) == 1:
						data[key]= {"end":True}
						return True
					else:
						data[key]= {}
						insDict(value[1:],data[key])

		insDict(name,self.data)

	def printDict(self):
		print (self.data)

if __name__ == "__main__":
	db = DictSearch()
	db.addValue("martha")
	db.addValue("jane")
	db.addValue("ja")
	db.addValue("jhon")
	db.printDict()