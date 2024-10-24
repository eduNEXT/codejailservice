Codejail service
================

|ci-badge| |license-badge|

The repository codejailservice manages execution of untrusted code in secure sandboxes. It is designed primarily for Python execution, but
can be used for other languages as well. The security is enforced with AppArmor.

The creation of Codejail service affects the way untrusted code is executed, because it runs in a separate
container from the one running the platform.

Usage
-----

Using with `Tutor`_
~~~~~~~~~~~~~~~~~~~

Run the instructions from tutor plugin.

Plugin: tutor-contrib-codejail (https://github.com/eduNEXT/tutor-contrib-codejail)

.. _Tutor: https://docs.tutor.overhang.io

Using service independently
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clone repo

.. code-block:: bash

    git clone git@github.com:eduNEXT/codejailservice.git

Create a virtual environment

.. code-block:: bash

    cd codejailservice
    virtualenv venv
    source venv/bin/activate

Install requirements

.. code-block:: bash

    make requirements

Run service

.. code-block:: bash

    make run

Enjoy the service!


How to Contribute
-----------------

Contributions are welcome! See our `CONTRIBUTING`_ file for more
information – it also contains guidelines for how to maintain high code
quality, which will make your contribution more likely to be accepted.

.. _CONTRIBUTING: https://github.com/eduNEXT/codejailservice/blob/main/CONTRIBUTING.rst

License
-------

This software is licensed under the terms of the AGPLv3.

.. |ci-badge| image:: https://github.com/eduNEXT/codejailservice/actions/workflows/ci.yml/badge.svg?branch=main
    :target: https://github.com/eduNEXT/codejailservice/actions
    :alt: CI

.. |license-badge| image:: https://img.shields.io/github/license/eduNEXT/codejailservice
    :target: https://github.com/eduNEXT/codejailservice/blob/main/LICENSE
    :alt: License
