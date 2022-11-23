import settings
import unittest
from django.test import Client

def foo():
    cli = Client()
    return cli.get('/')

class MyTest(unittest.TestCase):
    def test(self):
        response = foo()
        self.assertEqual(200, response.status_code)
        self.assertEqual(b'Hello World', response.content)

if __name__ == '__main__':
    unittest.main()

# python3 ./step-006/manage.py test tests
# python3 ./step-006/tests.py