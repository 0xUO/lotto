from application import app, routes
import application.routes
from flask_testing import TestCase
from unittest.mock import patch 
from flask import url_for 

class TestBase(TestCase):
    def create_app(self):
        return app

class TestView(TestBase):
    @patch('application.routes.choice', return_value='one')
    def test_get_magicNum_1(self, mock_func):
        response = self.client.get(url_for('magicNumber'))
        self.assert200(response)
        self.assertIn(b'one', response.data)

    @patch('application.routes.choice', return_value='two')
    def test_get_magicNum_2(self, mock_func):
        response = self.client.get(url_for('magicNumber'))
        self.assert200(response)
        self.assertIn(b'two', response.data)

    @patch('application.routes.choice', return_value='three')
    def test_get_magicNum_3(self, mock_func):
        response = self.client.get(url_for('magicNumber'))
        self.assert200(response)
        self.assertIn(b'three', response.data)

    @patch('application.routes.choice', return_value='four')
    def test_get_magicNum_4(self, mock_func):
        response = self.client.get(url_for('magicNumber'))
        self.assert200(response)
        self.assertIn(b'four', response.data)

    @patch('application.routes.choice', return_value='five')
    def test_get_magicNum_5(self, mock_func):
        response = self.client.get(url_for('magicNumber'))
        self.assert200(response)
        self.assertIn(b'five', response.data)
