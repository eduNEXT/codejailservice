"""Manage the app and config the codejail functionality."""

import os
import sys
from logging.config import dictConfig

from codejail import jail_code
from flask import Flask, logging

from .routes import routes

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "%(asctime)s %(levelname)s %(process)d "
                "[%(name)s] %(filename)s:%(lineno)d - %(message)s",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": sys.stdout,
                "formatter": "default",
            }
        },
        "root": {"level": "DEBUG", "handlers": ["console"]},
    }
)


def configure_codejail(application):
    """Logic to configure Flask app according to code."""
    code_jail_settings = application.config["CODE_JAIL"]
    python_bin = code_jail_settings.get("python_bin")
    if python_bin:
        user = code_jail_settings["user"]
        jail_code.configure("python", python_bin, user=user)
    limits = code_jail_settings.get("limits", {})
    for name, value in limits.items():
        jail_code.set_limit(
            limit_name=name,
            value=value,
        )
    limit_overrides = code_jail_settings.get("limit_overrides", {})
    for context, overrides in limit_overrides.items():
        for name, value in overrides.items():
            jail_code.override_limit(
                limit_name=name,
                value=value,
                limit_overrides_context=context,
            )


# ####################### APP CONFIGURATION #####################

app = Flask(__name__)

env_config = os.getenv("FLASK_APP_SETTINGS", "codejailservice.config.ProductionConfig")
app.config.from_object(env_config)

configure_codejail(app)

LOG = logging.create_logger(app)
app.register_blueprint(routes)
