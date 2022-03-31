class model():
	#recibe URL to be consummed in order to bring back a response
	def __init__(self,id):
		self.id = id

	def getData(self):
		#emulate the response from DB
		if self.id=="1":
			data = {}
			data['nombre'] = 'Jose'
			data['edad'] = '15'
			data['nacionalidad'] = 'Mex'
		else: 
			data="null"
		#response raw response to the controller
		return data