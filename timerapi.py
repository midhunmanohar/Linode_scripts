import flask
from flask import request, jsonify
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
def get_time():
    with open(r'/root/python_api/timer1.json') as json_file:
        f= json.load(json_file)
        return f

def porchlight_time():
    with open(r'/root/python_api/porch_timer.json') as json_file:
        f= json.load(json_file)
        return f


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/timeset', methods=['GET'])
def timeset():
    data = get_time()
    print(data['ontime'])
    print(data["offtime"])
    return jsonify(data)

@app.route('/api/porchlighttimer', methods=['GET'])
def porchtimeset():
    data = porchlight_time()
    print(data['ontime'])
    print(data["offtime"])
    return jsonify(data)
app.run("0.0.0.0",5003)
