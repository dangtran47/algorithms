
import unittest
from round_robin import RoundRobinLoadBalancer
from server import Server

class TestRoundRobinLoadBalancer(unittest.TestCase):
    def setUp(self):
        self.server1 = Server('server1')
        self.server2 = Server('server2')
        self.server3 = Server('server3')

        self.load_balancer = RoundRobinLoadBalancer([self.server1, self.server2, self.server3])

    def test_next_server_servers_is_not_empty(self):
        # Test when servers are available
        self.assertEqual(self.load_balancer.next_server(), self.server1)
        self.assertEqual(self.load_balancer.next_server(), self.server2)
        self.assertEqual(self.load_balancer.next_server(), self.server3)

        # Test when reaching the end of the server list
        self.assertEqual(self.load_balancer.next_server(), self.server1)

    def test_next_server_when_servers_in_empty(self):
        empty_load_balancer = RoundRobinLoadBalancer([])
        with self.assertRaises(Exception):
            empty_load_balancer.next_server()

if __name__ == '__main__':
    unittest.main()