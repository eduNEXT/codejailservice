"""Testing the app functionality."""
import unittest

import requests

APP_ROUTE = "http://localhost:8550"


class CodejailserviceTest(unittest.TestCase):
    """
    Test case for Codejail Service
    """

    def test_works(self):
        assert True

    def test_main_route(self):
        """This run that the main route app is working and sending a text."""
        response = requests.get(APP_ROUTE)

        assert response.status_code == 200
        assert isinstance(response.text, str)

    def test_health_route(self):
        """This run that the health route  app is working and sending a text."""
        response = requests.get(f"{APP_ROUTE}/health")

        assert response.status_code == 200
        assert isinstance(response.text, str)
