"""

"""
import logging
import json
from copy import deepcopy

from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from codejail.safe_exec import SafeExecException, json_safe
from codejail.safe_exec import not_safe_exec as codejail_not_safe_exec
from codejail.safe_exec import safe_exec as codejail_safe_exec
from six import text_type

LOG = logging.getLogger(__name__)


class CodeExec(APIView):
    """
    CodeExec APIView.
    """

    def post(self, request):
        """
        View to execute code using codejail.
        """     
        payload = json.loads(request.data["payload"])
        globals_dict = deepcopy(payload["globals_dict"])

        unsafely = payload["unsafely"]
        if unsafely:
            exec_fn = codejail_not_safe_exec
        else:
            exec_fn = codejail_safe_exec

        try:
            python_path=payload["python_path"]
            extra_files=[(python_path[0], request.data[python_path[0]].read())]

            exec_fn(
                payload["code"],
                globals_dict,
                python_path=python_path,
                extra_files=extra_files,
                limit_overrides_context=payload["limit_overrides_context"],
                slug=payload["slug"],
            )
            
        except SafeExecException as e:
            # Saving SafeExecException e in exception to be used later.
            exception = e
            emsg = text_type(e)
        else:
            exception = None
            emsg = None

        response = {
            "globals_dict": globals_dict,
            "emsg": emsg
        }
        return JsonResponse(response, status=status.HTTP_200_OK, safe=False)
