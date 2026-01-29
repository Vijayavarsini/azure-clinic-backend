from flask import Flask, request, jsonify
from config import SQLALCHEMY_DATABASE_URI
from models import db, Patient

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route("/")
def home():
    return "Backend running"

# ---------------- CREATE ----------------
@app.route("/patients", methods=["POST"])
def create_patient():
    data = request.json

    patient = Patient(
        name=data["name"],
        age=data["age"],
        gender=data.get("gender"),
        phone=data.get("phone")
    )

    return jsonify({"message": "Patient created (logic only)"}), 201


# ---------------- READ ----------------
@app.route("/patients", methods=["GET"])
def get_patients():
    return jsonify({"message": "Fetch all patients (logic only)"})


# ---------------- UPDATE ----------------
@app.route("/patients/<int:id>", methods=["PUT"])
def update_patient(id):
    data = request.json
    return jsonify({"message": f"Update patient {id} (logic only)"})


# ---------------- DELETE ----------------
@app.route("/patients/<int:id>", methods=["DELETE"])
def delete_patient(id):
    return jsonify({"message": f"Delete patient {id} (logic only)"})

if __name__ == "__main__":
    app.run(debug=True)