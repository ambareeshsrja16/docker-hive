#!/usr/bin/env python
from elasticsearch import Elasticsearch, helpers
import sys, csv

# Create the elasticsearch client.
es = Elasticsearch(host = "elastic", port = 9200)

# Open csv file and bulk upload
with open(sys.argv[1]) as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index=sys.argv[2])
