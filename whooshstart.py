#this is the whoosh python file
#use this to make your search engine
# aka an index
# whoosh has good documentation
# be patient and work through it and you'll learn a lot! 
# --- be patient: I am projecting a bit because, sometimes, if I can't find an
# --- answer in the first few seconds, I stop reading.  I need patience.
# http://whoosh.readthedocs.io/en/latest/intro.html


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

# Below is importing the json files and adding them to the index.

#why do I have two of these things that look similiar
#It is because the different types of json files. One (pixar.json) has a bunch 
#of different films / json things in it. 
# The focus features json files only have one film in them.
# so parsing those required different ways. I probably could have go it to work
# with an if or try statement, but I was in a hurry and did it this way!

data_path = os.path.normpath(os.path.join(os.getcwd(), 'data'))
#data_path = os.path.normpath(os.path.join(os.getcwd()))
for root, dirs, files in os.walk(data_path):
    for file in [f for f in files if f.endswith('.json')]:
        file_path = os.path.join(data_path, file)
        with open(file_path) as f:
            #print(file_path)
            data = json.loads(''.join(f.readlines()))
            #print(data["_type"])
            try:
                writer.add_document(name=data['_type'], description=''.join(data['description']), path=data['url'])
            except:
                continue
            
for root, dirs, files in os.walk(data_path):
    for file in [f for f in files if f.endswith('.json')]:        
        file_path = os.path.join(data_path, file)
        with open(file_path) as f:
            #print(file_path)
            data = json.loads(''.join(f.readlines()))    
            for a in data:
               # print(a,v)
                #input()
                #writer.add_document(name=a['_type'], description=''.join(a['description']), path=a['url'])
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
