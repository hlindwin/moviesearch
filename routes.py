from flask import Flask, render_template, request
# from models import db, User # TODO need to add in db to track what people are searching
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

      searchedtext = form.SearchField.data
      searchresults = searching(searchedtext)
      return render_template('index.html', form=form, results=searchresults, cats="cats")

  elif request.method == "GET":
    return render_template('index.html', form=form)

if __name__ == "__main__":
  app.run(debug=True)