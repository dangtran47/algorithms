import unittest
from least_connections import LeastConnectionsLoadBalancer
from server import Server

class TestLeastConnectionsLoadBalancer(unittest.TestCase):
    def setUp(self):
        self.server1 = Server('server1')
        self.server2 = Server('server2')
        self.server3 = Server('server3')
        self.load_balancer = LeastConnectionsLoadBalancer(
            [
							self.server1,
              self.server2,
              self.server3
						]
				)

    def test_next_server_servers_is_not_empty(self):
        self.assertEqual(self.load_balancer.next_server(), self.server1)
        self.assertEqual(self.load_balancer.next_server(), self.server2)
        self.assertEqual(self.load_balancer.next_server(), self.server3)

        self.assertEqual(self.load_balancer.next_server(), self.server1)
        self.assertEqual(self.load_balancer.next_server(), self.server2)
        self.assertEqual(self.load_balancer.next_server(), self.server3)

        self.assertEqual(self.load_balancer.next_server(), self.server1)
        self.assertEqual(self.load_balancer.next_server(), self.server2)

        self.load_balancer.release_connection(self.server2)
        self.assertEqual(self.load_balancer.next_server(), self.server2)

        self.load_balancer.release_connection(self.server3)
        self.assertEqual(self.load_balancer.next_server(), self.server3)

    def test_next_server_when_servers_in_empty(self):
        empty_load_balancer = LeastConnectionsLoadBalancer([])
        with self.assertRaises(Exception):
            empty_load_balancer.next_server()

if __name__ == '__main__':
    unittest.main()