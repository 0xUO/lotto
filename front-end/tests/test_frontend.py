from application import app, db
from application.models import Results
from flask import url_for
import requests_mock
from flask_testing import TestCase
import pytest

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
                DEBUG = True,
                )
        return app

    def setUp(self):
        db.create_all()
        sample_result = Results(magicNumber='one', lottoDraw='[11, 12, 13, 14, 15]', prize='100')       
        db.session.add(sample_result)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestView(TestBase):
    def test_get_frontend(self):
        with requests_mock.Mocker() as m:
            m.get('http://lotto-api:5000/get-magicNumber', json={'magicNumber':'two'})
            m.get('http://lottodraw-api:5000/get-draw', json={'lottoDraw': '[11, 12, 13, 14, 15]'})
            m.post('http://prize-api:5000/prize', json={'prize':'200'})
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'[11, 12, 13, 14, 15] is the lottery draw!, Your Magic Number is one which wins you a 100 pounds bonus !!!', response.data)