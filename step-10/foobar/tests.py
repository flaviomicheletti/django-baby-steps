import foo.settings
# import unittest
from django.test import TestCase
from django.test import Client

def foo():
    cli = Client()
    return cli.get('/')

# class MyTest(unittest.TestCase):
class MyTest(TestCase):
    def test(self):
        response = foo()
        self.assertEqual(200, response.status_code)
        self.assertEqual(b'Hello World', response.content)

# if __name__ == '__main__':
    # unittest.main()


# python3 ./step-010/manage.py test foobar