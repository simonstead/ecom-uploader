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
    def test_can_fire_product_add_event(self):
        event_stream = EventStream()
        uploader = Uploader(event_stream)
        uploader.product_add(test_product)

        event = event_stream.stream[0]
        self.assertTrue(type(event['timestamp']) is datetime)
        self.assertEqual(event['type'], PRODUCT_ADD)

    def test_can_read_product_csv(self):
        events = EventStream()
        uploader = Uploader(events)
        uploader.read_products('data/test_products.csv')
        self.assertEqual(len(events.stream), 4)
        e = events.stream[1]
        self.assertEqual(e['type'], PRODUCT_ADD)
        self.assertEqual(e['body']['name'], 'testname')

    def test_fires_new_upload_event(self):
        events = EventStream()
        uploader = Uploader(events)
        uploader.read_products('data/test_products.csv')
        self.assertEqual(events.stream[0]['type'], PRODUCT_UPLOAD)
