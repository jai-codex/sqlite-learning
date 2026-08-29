from flask import Flask, request, jsonify
from database import get_connection

app = Flask(__name__)

@app.route("/farmers/<int:farmer_id>", methods=["GET"])
def get_farmers(farmer_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM farmers WHERE ID =?",
        (farmer_id,))

    farmer = cursor.fetchone()

    conn.close()

    if farmer is None:
        return jsonify({
            "message" : "Farmer not found!"
        })

    return jsonify({
        "Id" : farmer[0],
        "Name" : farmer[1],
        "Phone" : farmer[2]
    })

if __name__ == "__main__":
    app.run(debug=True)
