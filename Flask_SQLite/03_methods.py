from flask import Flask, request

app = Flask(__name__)

@app.route("/farmers", methods=["GET"])
def get_farmers():
    return "Here are the farmers"

@app.route("/farmers", methods=["POST"])
def add_farmers():

    data = request.json

    return f"Farmer received: {data["name"]}"

if __name__ == "__main__":
    app.run(debug=True)