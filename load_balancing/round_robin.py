from load_balancer import LoadBalancer

class RoundRobinLoadBalancer(LoadBalancer):
	def __init__(self, servers):
		super().__init__(servers)
		self.next_server_index = 0

	def next_server(self):
		if not self.servers:
			raise Exception("No servers available.")

		server = self.servers[self.next_server_index]
		self.next_server_index = (self.next_server_index + 1) % self.server_count
		return server