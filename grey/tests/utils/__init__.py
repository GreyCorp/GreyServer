"""
Grey General Test
"""
import unittest, os

from mock import patch
import motor

from grey.config import MONGODB
import grey.db

class GreyTest(unittest.TestCase):
    port = 7000
    
    def setUp(self):
        super(GreyTest, self).setUp()
        self.client = motor.MotorClient(MONGODB)
        grey.db.mongodb = self.client.testing

    def tearDown(self):
        super(GreyTest, self).tearDown()
        self.client.drop_database("testing")
