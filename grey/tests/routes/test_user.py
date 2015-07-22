"""
Grey Test Suite
Routes > User
"""
import unittest

from grey.tests.utils.server import server, post
from grey.tests.utils import GreyTest
from grey.routes.user import UserRoute
from grey.routes.auth import AuthRoute

ROUTES = [UserRoute, AuthRoute]


user_data = { "user": { "name": "yo", "location": "your ass" } }
headers = { "phone": "7034748272", "device": "device" }

class UserRouteTest(GreyTest):
    port = 7000

    @server(port, ROUTES)
    def test_non_authenticated(self):
        result = post(self.port, "user/create", user_data, headers)

        self.assertIn("data", result)
        self.assertEqual("User not authenticated", result["data"])

    @server(port, ROUTES)
    def test_missing_credentials(self):
        result = post(self.port, "user/create", user_data, {})
        self.assertEquals(result["status"], 401)

    @server(port, ROUTES)
    def test_create(self):
        # headers for auth/login is used for request params
        post(self.port, "auth/login", headers)
        user = post(self.port, "user/create", user_data, headers)
        self.assertIn("data", user)
        self.assertIn("userId", user["data"])
        self.assertIn("name", user["data"])

        # check if the client is trying to create an existing user
        user = post(self.port, "user/create", user_data, headers)
        self.assertIn("data", user)
        self.assertIn("userId", user["data"])
        self.assertIn("name", user["data"])

    @server(port, ROUTES)
    def test_update(self):
        update_dic = { "update_dic":
                { "new_field": "new what?", "location": "is dis updated" }
        }
        # headers for auth/login is used for request params
        post(self.port, "auth/login", headers)
        post(self.port, "user/create", user_data, headers)
        user = post(self.port, "user/update", update_dic, headers)

        self.assertIn("data", user)
        self.assertIn("userId", user["data"])
        self.assertIn("new_field", user["data"])
        self.assertIn("location", user["data"])
        self.assertEqual(
            update_dic["update_dic"]["location"],
            user["data"]["location"]
        )

if __name__ == "__main__":
    unittest.main()
