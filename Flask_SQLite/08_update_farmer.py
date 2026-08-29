from database import get_connection
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/farmers/<int:farmer_id>", methods=["PUT"])

def update_farmer(farmer_id):

    data = request.json

    name = data["name"]
    phone = data["phone"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE farmers SET name=?, phone=? WHERE ID=?",
        (name, phone, farmer_id))

    conn.commit()
    conn.close()

    return jsonify({
        "message" : "Updated successfully!"
    })
        
if __name__ == "__main__":
    app.run(debug=True)