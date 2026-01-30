def validate_patient(data):
    if "name" not in data or not isinstance(data["name"], str) or not data["name"].strip():
        return "Name is required and must be a non-empty string"

    if "age" not in data:
        return "Age is required"

    try:
        age = int(data["age"])
        if age <= 0:
            return "Age must be greater than 0"
    except:
        return "Age must be a number"

    if "phone" in data and data["phone"]:
        phone = str(data["phone"])
        if not phone.isdigit() or len(phone) != 10:
            return "Phone number must be exactly 10 digits"

    return None