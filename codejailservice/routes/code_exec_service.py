"""Route for evaluate code with post method in `/api/v0/code-exec`."""

import importlib
import json
import timeit
from copy import deepcopy

from flask import current_app, jsonify, request

from .config import routes


def import_code_jail_safe_exec():
    """Import  code_jail_functions in lazy way."""
    code_jail_safe_exec = importlib.import_module("codejail.safe_exec")
    safe_exec_exception = code_jail_safe_exec.SafeExecException
    codejail_not_safe_exec = code_jail_safe_exec.not_safe_exec
    codejail_safe_exec = code_jail_safe_exec.safe_exec

    return safe_exec_exception, codejail_not_safe_exec, codejail_safe_exec


@routes.post("/api/v0/code-exec")
def code_exec():
    """Code-exec route logic for post."""
    log = current_app.logger

    # Lazy imports of codejail functions according(after) the configuration  app.
    (
        safe_exec_exception,
        codejail_not_safe_exec,
        codejail_safe_exec,
    ) = import_code_jail_safe_exec()

    payload = json.loads(request.form["payload"])
    globals_dict = deepcopy(payload["globals_dict"])

    unsafely = payload["unsafely"]
    if unsafely:
        exec_fn = codejail_not_safe_exec
    else:
        exec_fn = codejail_safe_exec

    try:
        python_path = payload["python_path"]
        if python_path:
            extra_files = [(python_path[0], request.files[python_path[0]].read())]
        else:
            extra_files = []
        course_id = payload["limit_overrides_context"]
        problem_id = payload["slug"]
        log.info(
            "Running problem_id:%s jailed code for course_id:%s ...",
            problem_id,
            course_id,
        )
        start = timeit.default_timer()
        exec_fn(
            payload["code"],
            globals_dict,
            python_path=python_path,
            extra_files=extra_files,
            limit_overrides_context=course_id,
            slug=problem_id,
        )
        end = timeit.default_timer()

    except safe_exec_exception as exception:
        # Saving SafeExecException  in exception to be used later.
        log.error("Error found while executing jailed code.")
        emsg = str(exception)
    else:
        log.info("Jailed code was executed in %s seconds.", str(end - start))
        exception = None
        emsg = None

    response = {"globals_dict": globals_dict, "emsg": emsg}

    return jsonify(response)
