"""Route for default or main endpoint."""

from flask import Response

from .routes_config import routes


@routes.route("/")
def index():
    """Make a welcome message to give an idea of what this service entails."""
    return Response("Edx Codejail Service", status=200)
