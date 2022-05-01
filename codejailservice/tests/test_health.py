"""Testing the app functionality."""
from codejailservice.tests import BaseTestCase


class ServiceHealthTest(BaseTestCase):
    """
    Test cases for health endpoint.
    """

    def setUp(self):
        """Set shared conditions for tests."""
        super().setUp()
        self.service_url = f"{self.APP_ROUTE}/health"

    def test_health_route(self):
        """
        Get /health endpoint.

        Expected result:
            - OK status code.
            - The response text corresponds with the expected.
        """
        response = self.client.get(self.service_url)

        self.assertEqual(200, response.status_code)
        self.assertEqual("OK", response.text)
