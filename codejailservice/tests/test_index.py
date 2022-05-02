"""Testing the app functionality."""
from codejailservice.tests import BaseTestCase


class ServiceIndexTest(BaseTestCase):
    """
    Test cases for Index endpoint.
    """

    def setUp(self):
        """Set shared conditions for tests."""
        super().setUp()
        self.service_url = f"{self.APP_ROUTE}/"

    def test_index_route(self):
        """
        Get /index endpoint.

        Expected result:
            - OK status code.
            - The response text corresponds with the expected.
        """
        response = self.client.get(self.service_url)

        self.assertEqual(200, response.status_code)
        self.assertEqual("Edx Codejail Service", response.text)
