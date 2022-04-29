from flask import Flask, render_template, request, session, send_file, jsonify, make_response
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS
import boto3

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

@app.route('/whereIsRunnig', methods=['GET'])
@app.route('/whereIsRunnig/', methods=['GET'])
def where_is_running():
    instance_id = (requests.get("http://169.254.169.254/latest/meta-data/instance-id")).text
    
    ec2 = boto3.resource('ec2', region_name="us-east-1")
    ec2instance = ec2.Instance(instance_id)
    
    cluster_type = {"type" : "Managed", "platform" : "EKS"}
    
    for tags in ec2instance.tags:
        if "kops" in tags['Key']:
            cluster_type = {"type" : "Self-Managed", "platform" : "kOps"}
            break
    
    response = make_response(
                jsonify(cluster_type),
                200,
            )
    response.headers["Content-Type"] = "application/json"
    
    return response

    
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)