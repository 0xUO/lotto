from application import app, routes
import application.routes
from flask_testing import TestCase
from unittest.mock import patch 
from flask import url_for 
from random import sample
import random

class TestBase(TestCase):
    def create_app(self):
        return app

class TestView(TestBase):
    def test_lottoDraw(self):
        with patch('random.sample') as r:
            r.return_value = '2,43,23,21,34'
            response = self.client.get(url_for('lottoDraw'))
            self.assert200(response)
            self.assertIn(b'2,43,23,21,34', response.data)


