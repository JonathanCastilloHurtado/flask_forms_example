from model import *

class controller():
	#reciibe URL from View in order to be consumed by model
	#some cases can be constructed adding some params to the URL base
	def __init__(self,person):
		self.person = person

	def saveData(self):
		return 'INSERT INTO USERS VALUES ('+self.person.usr+','+self.person.psw+','+self.person.address+','+self.person.city+','+self.person.state+','+self.person.zipCode+');'