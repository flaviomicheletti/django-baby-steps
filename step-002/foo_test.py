import foo
import unittest


def foo():
    return True


class MyTest(unittest.TestCase):
    def test(self):
        response = foo()
        self.assertEqual(True, foo())


if __name__ == '__main__':
    unittest.main()
