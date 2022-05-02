Purpose of this Repo
=======================

Status
------

Accepted

Context
-------

Codejailservice is a service that manages execution of untrusted code in secure sandboxes. It's useful
because allows executing code outside of ``edx-platform``, avoiding security risks on servers, limiting
staff permissions in some Open edx releases.

Decision
--------

create a codejail independent service that manages the execution of untrusted code in secure sandboxes.

Consequences
------------

The creation of codejailservice affects the way untrusted code is executed, because it runs in a separate
container from the one running the platform.