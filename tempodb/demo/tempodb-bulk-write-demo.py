"""
http://tempo-db.com/api/write-series/#bulk-write-multiple-series
"""

import datetime
from tempodb import Client

client = Client('your-api-key', 'your-api-secret')

ts = datetime.datetime.now()
data = [
    { 'key': 'custom-series-key1', 'v': 1.11 },
    { 'key': 'custom-series-key2', 'v': 2.22 },
    { 'key': 'custom-series-key3', 'v': 3.33 },
    { 'key': 'custom-series-key4', 'v': 4.44 },
]

print client.write_bulk(ts, data)
