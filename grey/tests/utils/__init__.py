"""
Grey General Test
"""
import unittest, os

import grey.db

DIR = os.path.dirname(grey.db.__file__)
collection_names = [
    name.split(".")[0] for name in os.listdir(DIR)
    if ".py" == name[-3:]
]

class GreyTest(unittest.TestCase):
    def tearDown(self):
        for name in collection_names:
             grey.db.mongodb.drop_collection(name)
        super(GreyTest, self).tearDown()
