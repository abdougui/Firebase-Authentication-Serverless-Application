# main.py
import functions_framework
from flask import jsonify, request
from auth import AuthService
from utils import validate_email_password

# Initialize the AuthService with your Firebase Admin SDK key
auth_service = AuthService(credentials_path="path/to/serviceAccountKey.json")

@functions_framework.http
def user_handler(request):
    path = request.path.lower()

    if path.endswith("/signup"):
        return signup_user(request)
    elif path.endswith("/signin"):
        return signin_user(request)
    else:
        return jsonify({"error": "Invalid endpoint"}), 404


def signup_user(request):

    try:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        # Validate input
        is_valid, error_message = validate_email_password(email, password)
        if not is_valid:
            return jsonify({"error": error_message}), 400

        # Perform sign-up
        result = auth_service.signup(email, password)
        if "error" in result:
            return jsonify(result), 500

        return jsonify(result), 201
    except Exception as e:
        return jsonify({"error": f"Error: {str(e)}"}), 500


def signin_user(request):
    try:
        data = request.get_json()
        id_token = data.get("id_token")

        # Validate input
        if not id_token:
            return jsonify({"error": "ID token is required"}), 400

        # Perform sign-in and verify ID token
        result = auth_service.signin(id_token)
        if "error" in result:
            return jsonify(result), 500

        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": f"Error: {str(e)}"}), 500
