from flask import *
import json, time

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage(_):
    dataset={"Page": "Home", "Message": "successfully loaded the Home page", "Timestamp":time.time}
    json_dump = json.dumps(dataset)

    return json_dump


@app.route('/user', methods=['GET'])
def homepage(_):
    dataset={"Page": "Home", "Message": "successfully loaded the Home page", "Timestamp":time.time}
    json_dump = json.dumps(dataset)

    return json_dump