import unittest
from app import app

class FlaskTest(unittest.TestCase):
    def test_hello(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.data, b"Hello, Neha!")

if __name__ == "__main__":
    unittest.main()

