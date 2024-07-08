import unittest
import json
from flaskr import create_app, db
from flaskr.models import Plant

class PlantTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
       
    def test_get_paginated_plants(self):
        res = self.client().get('/')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_plants'])
        self.assertTrue(len(data['plants']))
    
    def test_404_request_beyond_valid_page(self):
        res = self.client().get('/books?page=50', json={'rating':2})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

if __name__ == '__main__':
    unittest.main()