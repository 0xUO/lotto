from application import app, routes
from flask_testing import TestCase
from flask import url_for 

class TestBase(TestCase):
    def create_app(self):
        return app

class TestView(TestBase):
    def test_get_prize_1(self):
        response = self.client.post(url_for('prize'), json={'magicNumber':'one'})
        self.assert200(response)
        self.assertIn(b'100', response.data)

    def test_get_prize_2(self):
        response = self.client.post(url_for('prize'), json={'magicNumber':'two'})
        self.assert200(response)
        self.assertIn(b'200', response.data)

    def test_get_prize_3(self):
        response = self.client.post(url_for('prize'), json={'magicNumber':'three'})
        self.assert200(response)
        self.assertIn(b'300', response.data)

    def test_get_prize_4(self):
        response = self.client.post(url_for('prize'), json={'magicNumber':'four'})
        self.assert200(response)
        self.assertIn(b'400', response.data)

    def test_get_prize_5(self):
        response = self.client.post(url_for('prize'), json={'magicNumber':'five'})
        self.assert200(response)
        self.assertIn(b'500', response.data)