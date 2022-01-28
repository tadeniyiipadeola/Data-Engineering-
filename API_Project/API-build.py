from flask import *
import json, time

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    dataset={"Page": "Home", "Message": "successfully loaded the Home page", "Timestamp":time.time()}
    json_dump = json.dumps(dataset)

    return json_dump


@app.route('/user/', methods=['GET'])
def request_page(_):
    user_query = str(request.args.get('user'))
    dataset={"Page": "Request", "Message": f"successfully got the request for {user_query}", "Timestamp":time.time}
    json_dump = json.dumps(dataset)

    return json_dump

if __name__ == "__main__":
    app.run(port=80)