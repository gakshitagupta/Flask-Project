from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/<string:names>/')
def imdb_ratings(names):
     url = "http://www.omdbapi.com/?s=" + names + "&apikey=45c8affe"
     data = requests.get(url).json()
    #  x = data["Search"]
     length = len(data["Search"])
     return render_template('index.html', movie=data, leng=length, i=0)

if __name__ == '__main__':
    app.run(debug=True)
    