from flask import Flask, request, jsonify
from config import SQLALCHEMY_DATABASE_URI
from models import db, Patient
from flask_cors import CORS
from errors import not_found_error, bad_request_error

app = Flask(__name__)

CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "Backend running"

# CREATE
@app.route("/patients", methods=["POST"])
def create_patient():
    data = request.json

    if not data:
        return bad_request_error("JSON body is required")

    if "name" not in data or "age" not in data:
        return bad_request_error("Name and age are required")

    patient = Patient(
        name=data["name"],
        age=data["age"],
        gender=data.get("gender"),
        phone=data.get("phone")
    )

    db.session.add(patient)
    db.session.commit()

    return jsonify({
        "message": "Patient created successfully",
        "id": patient.id
    }), 201

# READ
@app.route("/patients", methods=["GET"])
def get_patients():
    patients = Patient.query.all()

    result = []
    for p in patients:
        result.append({
            "id": p.id,
            "name": p.name,
            "age": p.age,
            "gender": p.gender,
            "phone": p.phone
        })

    return jsonify(result), 200

# UPDATE
@app.route("/patients/<int:id>", methods=["PUT"])
def update_patient(id):
    patient = Patient.query.get_or_404(id)
    data = request.json
    patient.name = data.get("name", patient.name)
    patient.age = data.get("age", patient.age)
    patient.gender = data.get("gender", patient.gender)
    patient.phone = data.get("phone", patient.phone)
    db.session.commit()
    return jsonify({"message": "Patient updated"})

# DELETE
@app.route("/patients/<int:id>", methods=["DELETE"])
def delete_patient(id):
    patient = Patient.query.get(id)

    if not patient:
        return not_found_error("Patient not found")

    db.session.delete(patient)
    db.session.commit()

    return jsonify({"message": "Patient deleted"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)