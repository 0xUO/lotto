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

    @patch('application.routes.sample', return_value=[2,43,23,21,34])
    def test_lottoDraw(self, mock_func):
        response = self.client.get(url_for('lottoDraw'))
        self.assert200(response)
