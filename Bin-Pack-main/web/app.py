import requests
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    response = requests.get('http://api:5000/newproblem')
    jsonResponse = response.json()
    problemID = jsonResponse['ID']
    

if __name__ == '__main__':
    app.run(port=5000)