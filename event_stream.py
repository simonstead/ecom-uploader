from datetime import datetime
import uuid

class EventStream():
    def __init__(self):
        self.stream = []

    def write(self, event):
        self.stream.append(event)

    def event(self, event_type, body=None):
        event = {
                'type': event_type,
                'uuid': uuid.uuid4().__str__(),
                'timestamp': datetime.now(),
                'body': body
        }
        self.write(event)
