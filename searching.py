from whoosh.qparser import QueryParser
from whoosh.index import open_dir

ix = open_dir("index")
def searching(searchtext='canni*'):

    with ix.searcher() as searcher:
        parser = QueryParser("description", ix.schema)
        myquery = parser.parse(searchtext)
        results = searcher.search(myquery, limit=None)
        # print(len(results))
        # print(results[0])
        resultsdict = {}
        resultslist = []
        index = 0

        for r in results:
            resultslist.append({'index':index, 'name':r['name'],'path':r['path'], 'description':r['description']})
            index +=1
        # print(resultslist)
        return(resultslist)

if __name__ == "__main__":
    searching()
