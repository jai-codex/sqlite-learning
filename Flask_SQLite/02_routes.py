from flask import Flask 

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"

@app.route("/farmers")
def farmers():
    return "Farmers Page"

@app.route("/crops")
def crops():
    return "Crops Page"

@app.route("/buyers")
def buyers():
    return "Buyers Page"
    
if __name__ == "__main__":
    app.run(debug=True)

