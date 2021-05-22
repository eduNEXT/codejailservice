"""

"""
import logging

from django.http import JsonResponse
from opaque_keys.edx.keys import CourseKey
from rest_framework import status
from rest_framework.views import APIView

from openedx_external_enrollments.edxapp_wrapper.get_courseware import get_course_by_id
from openedx_external_enrollments.edxapp_wrapper.get_edx_rest_framework_extensions import get_jwt_authentication
from openedx_external_enrollments.edxapp_wrapper.get_openedx_authentication import get_oauth2_authentication
from openedx_external_enrollments.edxapp_wrapper.get_openedx_permissions import get_api_key_permission
from openedx_external_enrollments.external_enrollments.salesforce_external_enrollment import SalesforceEnrollment
from openedx_external_enrollments.factory import ExternalEnrollmentFactory
from openedx_external_enrollments.tasks import generate_salesforce_enrollment

LOG = logging.getLogger(__name__)


class CodeExec(APIView):
    """
    CodeExec APIView.
    """

    def post(self, request):
        """
        View to execute the external enrollment.
        """
        response = {}

        return response