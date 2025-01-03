import unittest
from unittest.mock import patch, MagicMock
from main import signup_user, signin_user
from flask import Request


class TestAuthEndpoints(unittest.TestCase):

    def setUp(self):
        self.mock_request = MagicMock(spec=Request)

    @patch("auth.AuthService.signup")
    def test_signup_user_success(self, mock_signup):
        mock_signup.return_value = {"message": "User created successfully"}

        self.mock_request.get_json.return_value = {
            "email": "test@example.com",
            "password": "Test1234"
        }

        response = signup_user(self.mock_request)
        
        self.assertEqual(response.status_code, 201)
        self.assertIn("User created successfully", response.get_data(as_text=True))

    @patch("auth.AuthService.signup")
    def test_signup_user_invalid_email(self, mock_signup):
        mock_signup.return_value = {"error": "Invalid email format"}

        # Mock input data
        self.mock_request.get_json.return_value = {
            "email": "invalid-email",
            "password": "Test1234"
        }

        response = signup_user(self.mock_request)
        
        # Verify that the response is an error
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid email format", response.get_data(as_text=True))

    @patch("auth.AuthService.signin")
    def test_signin_user_success(self, mock_signin):
        mock_signin.return_value = {"message": "User signed in successfully"}

        self.mock_request.get_json.return_value = {"id_token": "valid_token"}

        response = signin_user(self.mock_request)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn("User signed in successfully", response.get_data(as_text=True))

    @patch("auth.AuthService.signin")
    def test_signin_user_invalid_token(self, mock_signin):
        mock_signin.return_value = {"error": "Invalid ID token"}

        self.mock_request.get_json.return_value = {"id_token": "invalid_token"}
        response = signin_user(self.mock_request)
        
        self.assertEqual(response.status_code, 500)
        self.assertIn("Invalid ID token", response.get_data(as_text=True))

    @patch("auth.AuthService.signin")
    def test_signin_missing_id_token(self, mock_signin):
        mock_signin.return_value = {"error": "ID token is required"}

        self.mock_request.get_json.return_value = {}

        response = signin_user(self.mock_request)

        self.assertEqual(response.status_code, 400)
        self.assertIn("ID token is required", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
