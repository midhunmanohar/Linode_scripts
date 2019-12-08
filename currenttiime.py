import flask
from flask import request, jsonify
import json
import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
#def get_time():
#    with open(r'/root/python_api/timer1.json') as json_file:
#        f= json.load(json_file)
#        return f

#def porchlight_time():
#    with open(r'/root/python_api/porch_timer.json') as json_file:
#        f= json.load(json_file)
#        return f


#@app.route('/', methods=['GET'])
#def home():
#    return 


# A route to return all of the available entries in our catalog.
@app.route('/api/time', methods=['GET'])
def timeset():
    data={};
    data["time"] = datetime.datetime.now().strftime("%H")
    #data["time"] =19
    print(data)
    return jsonify(data)

app.run("0.0.0.0",5005)
