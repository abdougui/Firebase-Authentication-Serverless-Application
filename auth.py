import firebase_admin
from firebase_admin import auth, credentials

class AuthService:
    def __init__(self, credentials_path):
        # Initialize Firebase Admin SDK
        cred = credentials.Certificate(credentials_path)
        firebase_admin.initialize_app(cred)

    def signup(self, email, password):
        try:
            # Check if user already exists by email (optional for better UX)
            users = auth.list_users()
            for user in users.iterate_all():
                if user.email == email:
                    return {"error": "User already exists with this email address."}

            # Create user in Firebase Authentication
            user = auth.create_user(email=email, password=password)
            return {"message": "User created successfully", "uid": user.uid}
        except Exception as e:
            return {"error": f"Error during signup: {str(e)}"}

    def signin(self, id_token):
        try:
            # Verify the Firebase ID token
            decoded_token = auth.verify_id_token(id_token)
            uid = decoded_token['uid']  # Get user ID from decoded token
            return {"message": "User signed in successfully", "uid": uid}
        except Exception as e:
            return {"error": f"Error during sign-in: {str(e)}"}
