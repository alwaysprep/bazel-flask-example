import unittest

from src.python.ws import create_app


class BasicTestCase(unittest.TestCase):
    def test_if_root_path_exists(self):
        tester = create_app().test_client(self)
        response = tester.get("/", content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_if_fake_path_does_not_exist(self):
        tester = create_app().test_client(self)
        response = tester.get("/fake_path", content_type="html/text")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    import pytest
    import sys

    sys.exit(pytest.main([__file__]))
