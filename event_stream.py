from datetime import datetime
import uuid
import psycopg2
import psycopg2.extras
import json

class EventStream():
    def __init__(self):
        self.conn = psycopg2.connect("dbname=postgres host=postgres user=postgres")
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def __del__(self):
        self.cur.close()

    def stream(self):
        self.cur.execute("SELECT * FROM events;")
        return self.cur.fetchall()

    def write(self, event):
        try:
            self.cur.execute(
            """
                INSERT INTO 
                    events (type, uuid, body) 
                VALUES (%(type)s, %(uuid)s, %(body)s)
                   
            """, event)
        except Exception as e:
            raise(e)
        finally:
            self.conn.commit()

    def event(self, event_type, body={}):
        b = json.dumps(body)
        event = {
                'type': event_type,
                'uuid': uuid.uuid4().__str__(),
                'body': b
        }
        self.write(event)
