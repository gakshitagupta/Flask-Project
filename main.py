from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/<string:names>/')
def imdb_ratings(names):
     url = "http://www.omdbapi.com/?t=" + names + "&apikey=45c8affe"
     data = requests.get(url).json()
     x = data["Title"]
     y = data["Actors"]
     z = data['Ratings'][0]
     w = z['Value']
     return render_template('index2.html', movie=x, actor=y, rating=w)

if __name__ == '__main__':
    app.run(debug=True)
    