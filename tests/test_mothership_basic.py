
import unittest

from mothership.base import MothershipServer


class TestMothershipBasic(unittest.TestCase):
    pass

    def test_basic_mother_connection(self):

        mother = MothershipServer("https://www.reddit.com/user/Chrikelnel")

        self.assertRaises(ConnectionRefusedError, mother.run)
