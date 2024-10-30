from datetime import datetime

import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True
results = []

@app.route("/", methods=["GET"])
def home():
    if not results:
        response = dict(message="Most recent value not available")
    else:
        response = results[-1]
    return response, 200

@app.route("/recent", methods=["GET"])
def recent_results():
    return jsonify(results[-10:][::-1]), 200

@app.route("/all", methods=["GET"])
def all_results():
    return jsonify(results), 200

@app.route("/operate", methods=["GET"])
def operate():

    if "operation" in request.args:
        operation = request.args["operation"]
    else:
        return dict(error="Calculation Error", message="Invalid operation parameters"), 400
    result = 0
    try:
        if "+" in operation:
            operatee = operation.split("+")
            result = int(operatee[0]) + int(operatee[1])
        if "-" in operation:
            operatee = operation.split("-")
            result = int(operatee[0]) - int(operatee[1])
        if "*" in operation:
            operatee = operation.split("*")
            result = int(operatee[0]) * int(operatee[1])
        if "/" in operation:
            operatee = operation.split("/")
            result = int(operatee[0]) / int(operatee[1])
        response = {"updated_date": datetime.now(), "operation": operation, "result": result}
        results.append(response)
        return response, 200
    except Exception as e:
        return dict(error="Calculation Error", exception=str(e), message="Review operation parameters and try again"), 400

@app.errorhandler(404)
def page_not_found(error):
    return dict(response="This page does not exist"), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5755, debug=True)
