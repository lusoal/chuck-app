from flask import Flask, render_template, request, session, send_file, jsonify, make_response
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS

from get_images import *

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    response = make_response(
                jsonify(
                    {"message": "Hello from container"}
                ),
                200,
            )
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/randonFacts/', methods=['GET'])
@app.route('/randonFacts', methods=['GET'])
def random_facts():
    chuck_joke = requests.get("https://api.chucknorris.io/jokes/random")
    chuck_joke_str = (chuck_joke.json())
    
    image_url = get_google_images()
      
    response = make_response(
                jsonify(
                   {"Joke": chuck_joke_str.get('value'),
                    "Img": image_url}
                ),
                200,
            )
    response.headers["Content-Type"] = "application/json"
    return response

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)