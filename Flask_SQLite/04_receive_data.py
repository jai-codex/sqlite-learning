from flask import Flask, request

app = Flask(__name__)

@app.route("/farmers", methods=["POST"])
def add_farmer():

    data = request.json

    name = data["name"]
    phone = data["phone"]

    print("Name:", name)
    print("Phone:", phone)

    return "Farme data received!"

if __name__ == "__main__":
    app.run(debug=True)