from flask import Flask, request, jsonify
from database import get_connection

app = Flask(__name__)

@app.route("/farmers/<int:farmer_id>", methods=["DELETE"])
def delete_farmer(farmer_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM farmers WHERE ID=?",
        (farmer_id,))

    conn.commit()
    conn.close()

    return jsonify({
        "message" : "Farmer deleted successfully!"
    })    

if __name__ == "__main__":
    app.run(debug=True)