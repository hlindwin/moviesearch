# step 1: Make the schema

from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT

schema = Schema(name=TEXT(stored=True), description=TEXT(stored=True),
                path=ID(stored=True))

# step 2: Make the index

import os.path
from whoosh.index import create_in

if not os.path.exists("index"):
    os.mkdir("index")
ix = create_in("index", schema)

# step 3: add stuff to the index
writer = ix.writer()
import json
import os

data_path = os.path.normpath(os.path.join(os.getcwd(), 'data'))
#data_path = os.path.normpath(os.path.join(os.getcwd()))
for root, dirs, files in os.walk(data_path):
    for file in [f for f in files if f.endswith('.json')]:
        file_path = os.path.join(data_path, file)
        with open(file_path) as f:
            data = json.loads(''.join(f.readlines()))
            for a in data:

            #print(data[1]['description'][0], data[1]['_type'], data[1]["url"])
            # didn't work ---- print(data[]['description'][0], data[]['_type'], data[]["url"])

                try:
                    writer.add_document(name=a['_type'], description=''.join(a['description']), path=a['url'])
                    # TODO fix key errors
                except:
                    continue


writer.commit()

# step 4: seearching
from whoosh.qparser import QueryParser

with ix.searcher() as searcher:
    parser = QueryParser("description", ix.schema)
    myquery = parser.parse('cop')
    results = searcher.search(myquery, limit=None)
    print(len(results))
    print(results[0])
