from flask import Flask, request, jsonify
from farmer import add_farmer

app = Flask(__name__)

@app.route("/farmers", methods=["POST"])
def create_farmer():

    data = request.json

    name = data["name"]
    phone = data["phone"]

    add_farmer(name, phone)

    return jsonify({
        "message" : "Farmer added successfully!"
    })

if __name__ == "__main__":
    app.run(debug=True)    