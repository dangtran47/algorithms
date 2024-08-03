from load_balancer import LoadBalancer

class LeastConnectionsLoadBalancer(LoadBalancer):
	def __init__(self, servers):
		super().__init__(servers)

	def next_server(self):
		if not self.server_count:
			raise('No server')
			
		server_with_least_connections = min(self.servers, key=lambda s: s.connections)
		server_with_least_connections.connect()
		return server_with_least_connections

	def release_connection(self, server):
		for s in self.servers:
			if server == s:
				server.disconnect()
				break
		

