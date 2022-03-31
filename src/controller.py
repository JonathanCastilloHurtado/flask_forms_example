from model import *

class controller():
	#save person atributes into a DB
	def saveData(self,person):
		self.person = person
		#construct the SQL sentence in order to set it on the DB
		#if an insertion must be done by an API just construct an URL plus Query params instead a sql sentence
		#the return must bring back a status in order to be shown to final user previously parced by a method  like a requestUsr
		return 'INSERT INTO USERS VALUES ('+self.person.usr+','+self.person.psw+','+self.person.address+','+self.person.city+','+self.person.state+','+self.person.zipCode+');'

	#request a URL get petition based in a query param id	
	def requestUsr(self,mid):
		self.id = mid
		#initialize model to chain the MVC also send a id(can be an URL) to be recived by the constructor
		mModel = model(self.id)
		#response data(raw) from model are parced and restructured(diferents types of response as xml, json, etc..)
		response= mModel.getData()
		ABSOLUTE_RESPONSE= {}
		if response != "null":
			ABSOLUTE_RESPONSE['StatusCode'] = '200'
			ABSOLUTE_RESPONSE['statusMessage'] = 'Success'
			ABSOLUTE_RESPONSE['Results'] = response
		else:
			ABSOLUTE_RESPONSE['StatusCode'] = '404'
			ABSOLUTE_RESPONSE['statusMessage'] = 'Not found'
			ABSOLUTE_RESPONSE['Results'] = 'null'
		#return it to the viw to be shown	
		return ABSOLUTE_RESPONSE