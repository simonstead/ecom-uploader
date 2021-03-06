import csv
from event_types import *
from event_stream import EventStream

class Uploader():
    def __init__(self, event_stream=EventStream()):
        self.stream = event_stream

    def product_upload(self):
        self.stream.event(PRODUCT_UPLOAD)

    def product_add(self, product):
        self.stream.event(PRODUCT_ADD, product)

    def read_products(self, filename):
        self.product_upload()
        with open(filename, 'r') as products_file:
            reader = csv.DictReader(products_file)
            for p in reader:
                self.product_add(p)
            #map(lambda p: self.product_add(p), reader)
