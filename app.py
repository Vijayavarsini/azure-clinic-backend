from flask import Flask, request, jsonify
from config import SQLALCHEMY_DATABASE_URI
from models import db, Patient

app = Flask(__name__)
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
    patient = Patient(
        name=data["name"],
        age=data["age"],
        gender=data.get("gender"),
        phone=data.get("phone")
    )
    db.session.add(patient)
    db.session.commit()
    return jsonify({"message": "Patient created"}), 201

# READ
@app.route("/patients", methods=["GET"])
def get_patients():
    patients = Patient.query.all()
    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "age": p.age,
            "gender": p.gender,
            "phone": p.phone
        } for p in patients
    ])

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
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    return jsonify({"message": "Patient deleted"})

if __name__ == "__main__":
    app.run(debug=True)