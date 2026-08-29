from flask import Flask, request, jsonify
from database import get_connection

app = Flask(__name__)


@app.route("/farmers", methods=["POST"])
def add_farmer():

    data = request.json

    if not data:
        return jsonify({"error": "No data provided"}), 400

    if not data.get("name"):
        return jsonify({"error": "Name is required"}), 400

    if not data.get("phone"):
        return jsonify({"error": "Phone no is required"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO farmers(name, phone) VALUES(?, ?)",
            (data["name"], data["phone"]),
        )

        conn.commit()
    except Exception:
        conn.close()
        return jsonify({"error": "Could not add farmer"}), 500
    conn.close()
    return jsonify({"message": "Farmer added successfully!"}), 201


if __name__ == "__main__":
    app.run(debug=True)
