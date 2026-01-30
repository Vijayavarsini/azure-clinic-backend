from flask import Flask, request, jsonify
from config import SQLALCHEMY_DATABASE_URI
from models import db, Patient
from flask_cors import CORS
from errors import not_found_error, bad_request_error
from validators import validate_patient
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name": "Clinic Management API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route("/")
def home():
    return "Backend running"

# CREATE
@app.route("/patients", methods=["POST"])
def create_patient():
    data = request.json

    if not data:
        return bad_request_error("JSON body is required")

    error = validate_patient(data)
    if error:
        return bad_request_error(error)

    patient = Patient(
        name=data["name"].strip(),
        age=int(data["age"]),
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
    patient = Patient.query.get(id)

    if not patient:
        return not_found_error("Patient not found")

    data = request.json
    if not data:
        return bad_request_error("JSON body is required")

    error = validate_patient({**{
        "name": patient.name,
        "age": patient.age,
        "phone": patient.phone
    }, **data})

    if error:
        return bad_request_error(error)

    patient.name = data.get("name", patient.name)
    patient.age = int(data.get("age", patient.age))
    patient.gender = data.get("gender", patient.gender)
    patient.phone = data.get("phone", patient.phone)

    db.session.commit()

    return jsonify({"message": "Patient updated"}), 200

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
    app.run()