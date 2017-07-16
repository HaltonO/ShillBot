
import unittest

from mothership.base import MothershipServer


class TestMothershipBasic(unittest.TestCase):
    pass

    def test_basic_mother_connection(self):

        mother = MothershipServer("https://www.reddit.com/user/Chrikelnel")

        self.assertRaises(ConnectionRefusedError, mother.run)



    def test_worker_contact(self):

        contact = handle_worker_contact(self, worker, address):

        self.assertRaises(ConnectionRefusedError, worker.run)

    def send_mother(self):

        worker = BasicUserParseWorker("https://www.reddit.com/user/Chrikelnel")

        data = worker.recv(self.buff_size)
        original_target = None
        send_to_mother(self, data, original_target)
