from django.test import TestCase


class HomeViewsTestCase(TestCase):
    def test_home(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
