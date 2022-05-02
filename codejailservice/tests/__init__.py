"""Package for service test cases."""

import unittest

from codejailservice import app


class BaseTestCase(unittest.TestCase):
    """Base test case class for unittests."""

    APP_ROUTE = "http://localhost:8550"

    def setUp(self):
        """Set shared conditions for tests."""
        app.config.update({
            "TESTING": True,
        })
        self.client = app.test_client()
