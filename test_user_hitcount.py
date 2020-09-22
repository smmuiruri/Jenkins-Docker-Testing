import unittest
from unittest.mock import patch

# Mock for redis
import mockredis
import hitcount

class HitCountTest (unittest.TestCase):
    def testOneHit(self):
        # increase the hit count for user user1
        hitcount.hit("user1")
        # ensure that the hit count for user1 is just 1
        self.assertEqual(b'1', hitcount.getHit("user1"))

if __name__ == '__main__':
    unittest.main()