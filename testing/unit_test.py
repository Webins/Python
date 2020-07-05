# test smalles part of an application in isolation(units)
# individual classes, modules, functions
# you can write unit tests encapsulated as class than inherit from unittest.Testcase

import unittest

from activities import eat,nap

class ActivityTests(unittest.TestCase):

    def test_eat_healthy(self):
        """Testing eat healthy"""
        self.assertEqual(
            eat("broccoli", is_healthy=True),
            "I'm eating broccoli because is healthy"
        )
    
    def test_eat_unhealthy(self):
        """Testing eat unhealthy"""
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza because is delicious"
        )

    def test_eat_boolean(self):
        """Testing a boolean parameter"""
        with self.assertRaises(ValueError):
            eat("pizza", "?")

    def test_short_nap(self):
        """Testing short naps"""
        self.assertEqual(
            nap(1),
            "I'm feeling refreshed after my 1 hour nap"
        )
    
    def test_long_nap(self):
        """Testing long naps"""
        self.assertEqual(
            nap(3),
            "I'm feeling refreshed. But I sleep too much"
        )




    pass

if __name__ == "__main__":
    unittest.main()