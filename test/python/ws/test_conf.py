import unittest

from src.python.ws import create_app


class TestConfig(unittest.TestCase):
    def test_if_default_conf_is_set(self):
        app = create_app()
        self.assertEqual(app.config.get("DEBUG"), False)

    def test_if_development_conf_is_set(self):
        app = create_app("src.python.ws.conf.DevelopmentConfig")
        self.assertEqual(app.config.get("DEBUG"), True)

    def test_if_test_conf_is_set(self):
        app = create_app("src.python.ws.conf.TestingConfig")
        self.assertEqual(app.config.get("TESTING"), True)


if __name__ == "__main__":
    import sys
    import pytest

    sys.exit(pytest.main([__file__]))
