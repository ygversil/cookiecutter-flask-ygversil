"""Tests about homepage."""

import unittest

from {{ cookiecutter.project_slug }} import create_app, read_config

from . import TEST_CONFIG


class TestHomepageAnonymous(unittest.TestCase):
    """Check homepage as anonymous user."""

    def setUp(self):
        super(TestHomepageAnonymous, self).setUp()
        self.app = create_app(read_config(TEST_CONFIG))
        self.client = self.app.test_client()

    def test_homepage_content(self):
        resp = self.client.get('/')
        self.assertIn(b'{{ cookiecutter.project_name }} homepage', resp.data)
