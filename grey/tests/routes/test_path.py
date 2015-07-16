"""
grey Test Suite
Routes > Path
"""
import unittest

from grey.tests.utils.server import server, post
from grey.tests.utils import GreyTest
from grey.routes.path import PathRoute


ROUTES = [PathRoute]
class PathRouteTest(GreyTest):
    port = 7000

    @server(port, ROUTES)
    def test_create(self):
        result = post(self.port, "path/create", {
            "name": "Job",
            "creatorId": "randomCreatorId"
        })

        self.assertIn("data", result)
        self.assertIn("_id", result["data"])

if __name__ == "__main__":
    unittest.main()
