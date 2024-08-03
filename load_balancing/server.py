class Server:
	def __init__(self, name):
		self.name = name
		self.connections = 0
	
	def connect(self):
		self.connections += 1

	def disconnect(self):
		if self.connections > 0:
			self.connections -= 1
	
	def __repr__(self) -> str:
		return self.name

