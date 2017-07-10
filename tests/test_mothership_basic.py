
import unittest

from mothership.base import MothershipServer


class TestMothershipBasic(unittest.TestCase):
    pass

    def test_basic_mother_connection(self):

        mother = MothershipServer("https://www.reddit.com/user/Chrikelnel")

        # Can't connect to mother, so should raise ConnectionRefusedError, but should run everything else
        self.assertRaises(ConnectionRefusedError, mother.run)
