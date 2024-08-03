from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class LoadBalancer(ABC):
	"""
	Abstract base class for load balancers.
	"""

	def __init__(self, servers):
		self.server_count = len(servers)
		self.servers = servers

	@abstractmethod
	def next_server(self):
		"""
		Abstract method to get a server from the load balancer.
		Subclasses must implement this method.
		"""
		pass
