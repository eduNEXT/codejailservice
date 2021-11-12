"""Route for the Health response: `/health`."""

from flask import Response

from .routes_config import routes


@routes.route("/health")
def health():
    """Answer health route with response."""
    return Response("OK", status=200)
