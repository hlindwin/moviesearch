from flask import Flask, render_template, request
# from models import db, User #
from forms import SearchForm
#from searching import searching

app = Flask(__name__)

# TODO add back in a database to track all of the things people are searching
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
# db.init_app(app)

app.secret_key = "development-key"



@app.route("/", methods=["GET", "POST"])
def search():
  form = SearchForm()

  if request.method == "POST":

     # searchedtext = form.SearchField.data
     # searchresults = searching(searchedtext)
      return render_template('index.html', form=form) #, results=searchresults, cats="cats")

  elif request.method == "GET":
    return render_template('index.html', form=form)

if __name__ == '__main__':
  app.debug = True
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)

s = """from scrapy import Selector
import datetime
import json
import re

#from scrapy

#b = 'rawff.html'
b = 'ffbabies.html'
#response = open('other.html', 'r', errors='replace')
tree = open(b, encoding='utf-8', errors='replace')


tree = tree.read().splitlines()
for row in tree:
    if row.startswith('	GlobalsObj.CMS_JSON'):
        #print(row)
        description = re.findall(r"\{([^}]+)\}", row)
        print(description)"
        """
