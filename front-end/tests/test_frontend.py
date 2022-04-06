from application import app, db
from application.models import Results
from flask import url_for
import requests_mock
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            DEBUG = True
        )
        return app

    def setUp(self):
        sample_result = Results(magicNumber='one', lottoDraw='[11, 12, 13, 14, 15]', prize='100')
        db.create_all()
        db.session.add(sample_result)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestView(TestBase):
    def test_get_frontend(self):
        with requests_mock.Mocker() as m:
            m.get('http://lotto-api:5000/get-magicNumber', json={'magicNumber':'two'})
            m.get('http://lottodraw-api:5000/get-draw', json={'lottoDraw':'[16, 17, 18, 19, 20]'})
            m.post('http://prize-api:5000/prize', json={'prize':'200'})
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'[11, 12, 13, 14, 15] is the lottery draw!, Your Magic Number is one which wins you a 100 pounds bonus !!!', response.data)
            self.assertIn(b'[16, 17, 18, 19, 20] is the lottery draw!, Your Magic Number is two which wins you a 200 pounds bonus !!!', response.data)