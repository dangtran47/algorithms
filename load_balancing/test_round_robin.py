
import unittest
from round_robin import RoundRobinLoadBalancer

class TestRoundRobinLoadBalancer(unittest.TestCase):
    def setUp(self):
        self.load_balancer = RoundRobinLoadBalancer(['server1', 'server2', 'server3'])

    def test_next_server_servers_is_not_empty(self):
        # Test when servers are available
        self.assertEqual(self.load_balancer.next_server(), 'server1')
        self.assertEqual(self.load_balancer.next_server(), 'server2')
        self.assertEqual(self.load_balancer.next_server(), 'server3')

        # Test when reaching the end of the server list
        self.assertEqual(self.load_balancer.next_server(), 'server1')

    def test_next_server_when_servers_in_empty(self):
        empty_load_balancer = RoundRobinLoadBalancer([])
        with self.assertRaises(Exception):
            empty_load_balancer.next_server()

if __name__ == '__main__':
    unittest.main()