import unittest
from datetime import datetime
from uploader import Uploader
from event_types import *
from event_stream import EventStream


test_product = {
        'name': 'any_product_name',
        'quantity': 10,
        'description': 'any product description'
        }


class UploaderTests(unittest.TestCase):
    def setUp(self):
        self.events = EventStream()
        self.uploader = Uploader(self.events)

    def test_can_fire_product_add_event(self):
        self.uploader.product_add(test_product)
        event = self.events.stream()[0]

        self.assertTrue(type(event['inserted_at']) is datetime)
        self.assertEqual(event['type'], PRODUCT_ADD)

    def test_can_read_product_csv(self):
        old_length = len(self.events.stream())
        self.uploader.read_products('data/test_products.csv')
        new_length = len(self.events.stream())

        self.assertEqual(new_length, old_length + 4)

        e = self.events.stream()[old_length + 1]
        
        self.assertEqual(e['type'], PRODUCT_ADD)
        self.assertEqual(e['body']['name'], 'testname')

    def test_fires_new_upload_event(self):
        old_length = len(self.events.stream())
        self.uploader.read_products('data/test_products.csv')
        
        self.assertEqual(self.events.stream()[old_length]['type'], PRODUCT_UPLOAD)

