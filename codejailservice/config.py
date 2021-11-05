"""Module with the base, development and production class configuration."""
import os


class BaseConfig:
    """Class with the base case to use code_jail."""

    DEBUG = False
    DEVELOPMENT = False
    SECRET_KEY = os.getenv("SECRET_KEY", "this-is-the-default-key")

    CODE_JAIL = {
        "python_bin": "/sandbox/venv/bin/python",
        # User to run as in the sandbox.
        "user": "sandbox",
        # Configurable limits.
        # Setting all of them to 0 to disable limits in containers.
        "limits": {
            #
            "NPROC": 0,
            # How many CPU seconds can jailed code use?
            "CPU": 0,
            # Limit the memory of the jailed process to something high but not
            # infinite (512MiB in bytes)
            "VMEM": 0,
            # Time in seconds that the jailed process has to run.
            "REALTIME": 0,
            # Needs to be non-zero so that jailed code can use
            # it as their temp directory.(10MiB in bytes)
            "FSIZE": 10485760,
            # Disable usage of proxy (force thread-safe)
            "PROXY": 0,
        },
        # Overrides to default configurable 'limits' (above).
        # Keys should be course run ids.
        # Values should be dictionaries that look like 'limits'.
        "limit_overrides": {},
    }

    def __str__(self):
        """Make the string representation of the class."""
        return self.__class__.__name__


class DevelopmentConfig(BaseConfig):
    """Class to use for development context that inherits from BaseConfig."""

    DEBUG = True
    DEVELOPMENT = True


class ProductionConfig(BaseConfig):
    """Class to use for production context that inherits from BaseConfig."""
