"""
Grey Test Suite
Routes > Path
"""
import unittest

from grey.tests.utils.server import server, post
from grey.tests.utils import GreyTest
from grey.routes.auth import AuthRoute

ROUTES = [AuthRoute]

login_data = {
    "phone": "fakephone1",
    "device": "fakedevice1"
}

class AuthRouteTest(GreyTest):
    port = 7000

    @server(port, ROUTES)
    def test_login_created(self):
        result = post(self.port, "auth/login", login_data)

        self.assertIn("data", result)
        self.assertIn("_id", result["data"])
        _id = result["data"]["_id"]

        result = post(self.port, "auth/login", login_data)

        self.assertIn("data", result)
        self.assertIn("_id", result["data"])
        self.assertEqual(_id, result["data"]["_id"])

if __name__ == "__main__":
    unittest.main()
