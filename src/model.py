class model():
	#recibe URL to be consummed in order to bring back a response
	def __init__(self,mv):
		self.variable=mv+" Modelo"

	def getSaludo(self):
		#response raw response to the controller
		return self.variable