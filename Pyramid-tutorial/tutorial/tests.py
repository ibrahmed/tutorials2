import unittest

from pyramid import testing


class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from .views import home

        request = testing.DummyRequest()
        response = home(request)
        # Our view now returns data
        self.assertEqual('Home View', response['name'])

    def test_hello(self):
        from .views import form

        request = testing.DummyRequest()
        response = form(request)
        # Our view now returns data
        self.assertEqual('Form View', response['name'])


class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from tutorial import main
        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'<h1>Hi Home View', res.body)

    def test_form(self):
        res = self.testapp.get('/formd', status=200)
        self.assertIn(b'<h1>Hi Form View', res.body)
