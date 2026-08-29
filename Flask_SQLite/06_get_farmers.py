from flask import Flask, request, jsonify
from database import get_connection

app = Flask(__name__)

@app.route("/farmers", methods=["GET"])
def get_farmers():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM farmers")

    farmers = cursor.fetchall()

    conn.close()

    return jsonify(farmers) 

if __name__ == "__main__":
    app.run(debug=True)
