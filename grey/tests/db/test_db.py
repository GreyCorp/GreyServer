"""
Grey Test Suite
Db
"""
import unittest, time
from mock import patch

import motor
from tornado.ioloop import IOLoop
from bson.objectid import ObjectId

from grey.db import mongodb, auth_db
from grey.tests.utils.mongo import GreyAsyncTest

class DBTest(GreyAsyncTest):
    def test_db(self):
        self.assertIsInstance(mongodb, motor.MotorDatabase)

    def test_auth_db(self):
        self.assertIsInstance(mongodb.auth_db, motor.MotorCollection)

    def test_find_user_id(self):
        @self.callback
        def callback(result, error):
            self.assertIs(error, None)
            self.assertIs(result, None)

        hashed = "distincthash1"
        auth_db.find_user_id(hashed, callback)
        self.wait()

    def test_create_user(self):
        phone = "fakephonenumber"
        hashed = "distincthash2"

        # Create
        @self.callback
        def callback(result, error):
            self.assertIs(error, None)
            self.assertIsInstance(result, ObjectId)
        auth_db.create_user(phone, hashed, callback)
        self.wait()

        # Check if created
        @self.callback
        def check_created(result, error):
            self.assertIs(error, None)
            self.assertEqual(result["phone"], phone)
        auth_db.find_user_id(hashed, check_created)
        self.wait()

    def test_bad_calls(self):
        @self.callback
        def error_callback(result, error):
            self.assertIs(result, None)
            self.assertIsNot(error, None)
        random_object = object()
        auth_db.find_user_id(random_object, error_callback)
        self.wait()

if __name__ == "__main__":
    unittest.main()
