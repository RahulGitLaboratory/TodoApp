import unittest
import pytest
from starlette.testclient import TestClient
from ..main import app
from fastapi import status

client = TestClient(app)

def test_health_check():
    response = client.get("/healthy")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "healthy"}

'''class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
'''

if __name__ == '__main__':
    unittest.main()
