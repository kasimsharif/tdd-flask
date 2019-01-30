import json
import unittest

import os

from application import app, db


class TestChoiceList(unittest.TestCase):
    """Choice List Test Class"""

    def setUp(self):
        #self.app = create_app(config_name='testing')
        self.client = app.test_client
        self.choice_list = {'name': 'To see football match tonight'}

        with app.app_context():
            db.create_all()

    def test_choicelist_creation(self):
        """Test Choicelist creation (POST request)"""
        res = self.client().post('/choicelists/', data=json.dumps(self.choice_list))
        self.assertEqual(res.status_code, 201)
        self.assertIn('To see football match tonight', str(res.data))

    def test_get_all_choicelist(self):
        """Test Choicelist GET all"""
        res = self.client().post('/choicelists/', data=json.dumps(self.choice_list))
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/choicelists/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('To see football match tonight', str(res.data))

    def test_get_choice_list_by_id(self):
        """Test Choicelist GET call by id"""
        res = self.client().post('/choicelists/', data=json.dumps(self.choice_list))
        self.assertEqual(res.status_code, 201)
        data = json.loads(res.data)
        res = self.client().get('/choicelists/1/'.format(data['id']))
        self.assertEqual(res.status_code, 200)
        self.assertIn('To see football match tonight', str(res.data))

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == '__main__':
    if os.getenv('ENVIRONMENT', "testing") != "testing":
        print "set ENVIRONMENT to testing"
    else:
        unittest.main()
