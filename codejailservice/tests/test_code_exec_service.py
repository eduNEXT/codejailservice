"""Test classes for code_exec service."""
import json
from unittest import mock

from codejailservice.tests import BaseTestCase


class CodeExecServiceTest(BaseTestCase):
    """
    Test cases for Codejail Service.
    """

    def setUp(self):
        """Set shared conditions for tests."""
        super().setUp()
        self.service_url = f"{self.APP_ROUTE}/api/v0/code-exec"

    @mock.patch("codejailservice.routes.code_exec_service.import_code_jail_safe_exec")
    def test_safe_code_exec_success(self, import_code_jail_safe_exec):
        """
        Execute code using a safe execution method.

        Expected result:
            - Status code is successfull.
            - JSON response is equal to the expected result.
            - Safe method is called with appropriate arguments.
        """
        safe_exec, unsafe_exec = mock.Mock(), mock.Mock()
        import_code_jail_safe_exec.return_value = (
            Exception,
            unsafe_exec,
            safe_exec,
        )
        payload = {
            "code": "print('This is just a test!')",
            "globals_dict": {"seed": 1, "anonymous_student_id": "student"},
            "python_path": [],
            "limit_overrides_context": "course-v1:org+codejail-test+20XX",
            "slug": "string1",
            "unsafely": False,
        }
        expected_result = {
            "emsg": None,
            "globals_dict":
                {
                    "anonymous_student_id": "student", "seed": 1
                },
        }

        response = self.client.post(
            self.service_url,
            data={"payload": json.dumps(payload)},
        )

        self.assertEqual(200, response.status_code)
        self.assertDictEqual(expected_result, response.json)
        safe_exec.assert_called_once_with(
            payload["code"],
            payload["globals_dict"],
            python_path=payload["python_path"],
            extra_files=[],
            limit_overrides_context=payload["limit_overrides_context"],
            slug=payload["slug"],
        )
        unsafe_exec.assert_not_called()

    @mock.patch("codejailservice.routes.code_exec_service.import_code_jail_safe_exec")
    def test_unsafe_code_exec_success(self, import_code_jail_safe_exec):
        """
        Execute code using a unsafe execution method.

        Expected result:
            - Status code is successfull.
            - JSON response is equal to the expected result.
            - Unsafe method is called with appropriate arguments.
        """
        safe_exec, unsafe_exec = mock.Mock(), mock.Mock()
        import_code_jail_safe_exec.return_value = (
            Exception,
            unsafe_exec,
            safe_exec,
        )
        payload = {
            "code": "print('This is just a test!')",
            "globals_dict": {"seed": 1, "anonymous_student_id": "student"},
            "python_path": [],
            "limit_overrides_context": "course-v1:org+codejail-test+20XX",
            "slug": "string1",
            "unsafely": True,
        }
        expected_result = {
            "emsg": None,
            "globals_dict":
                {
                    "anonymous_student_id": "student", "seed": 1
                },
        }

        response = self.client.post(
            self.service_url,
            data={"payload": json.dumps(payload)},
        )

        self.assertEqual(200, response.status_code)
        self.assertDictEqual(expected_result, response.json)
        safe_exec.assert_called_once_with(
            payload["code"],
            payload["globals_dict"],
            python_path=payload["python_path"],
            extra_files=[],
            limit_overrides_context=payload["limit_overrides_context"],
            slug=payload["slug"],
        )
        unsafe_exec.assert_not_called()

    @mock.patch("codejailservice.routes.code_exec_service.import_code_jail_safe_exec")
    def test_unsafe_code_exec_failure(self, import_code_jail_safe_exec):
        """
        Execute invalid code using a unsafe execution method.

        Expected result:
            - Safe function that executes code is called with the appropriate arguments.
            - Unsafe function is not called.
        """
        safe_exec, unsafe_exec = mock.Mock(), mock.Mock()
        import_code_jail_safe_exec.return_value = (
            Exception,
            unsafe_exec,
            safe_exec,
        )
        safe_exec.side_effect = Exception("SyntaxError: invalid syntax ' with status code: 1")
        payload = {
            "code": "Syntax error",
            "globals_dict": {"seed": 1, "anonymous_student_id": "student"},
            "python_path": [],
            "limit_overrides_context": "course-v1:org+codejail-test+20XX",
            "slug": "string1",
            "unsafely": True,
        }
        expected_result = {
            "emsg": "SyntaxError: invalid syntax ' with status code: 1",
            "globals_dict":
                {
                    "anonymous_student_id": "student", "seed": 1
                },
        }

        response = self.client.post(
            self.service_url,
            data={"payload": json.dumps(payload)},
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_result['emsg'], response.json["emsg"])
        self.assertEqual(expected_result['globals_dict'], response.json["globals_dict"])
        unsafe_exec.assert_not_called()

    @mock.patch("codejailservice.routes.code_exec_service.import_code_jail_safe_exec")
    def test_safe_code_exec_failure(self, import_code_jail_safe_exec):
        """
        Execute invalid code using a safe execution method.

        Expected result:
            - Safe function that executes code is called with the appropriate arguments.
            - Unsafe function is not called.
        """
        safe_exec, unsafe_exec = mock.Mock(), mock.Mock()
        import_code_jail_safe_exec.return_value = (
            Exception,
            unsafe_exec,
            safe_exec,
        )
        safe_exec.side_effect = Exception("SyntaxError: invalid syntax ' with status code: 1")
        payload = {
            "code": "Syntax error",
            "globals_dict": {"seed": 1, "anonymous_student_id": "student"},
            "python_path": [],
            "limit_overrides_context": "course-v1:org+codejail-test+20XX",
            "slug": "string1",
            "unsafely": False,
        }
        expected_result = {
            "emsg": "SyntaxError: invalid syntax ' with status code: 1",
            "globals_dict":
                {
                    "anonymous_student_id": "student", "seed": 1
                },
        }

        response = self.client.post(
            self.service_url,
            data={"payload": json.dumps(payload)},
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_result['emsg'], response.json["emsg"])
        self.assertEqual(expected_result['globals_dict'], response.json["globals_dict"])
        unsafe_exec.assert_not_called()
