# Firebase Authentication Serverless Application

This is a sample **Serverless Application** built using **Google Cloud Run** and **Firebase Authentication**. The project demonstrates how to integrate Firebase Authentication with a serverless architecture, allowing users to sign up, sign in, and manage authentication via Firebase.

## Project Overview

This project uses:

- **Google Cloud Run** for serverless deployment.
- **Firebase Authentication** for handling user sign-ups, sign-ins, and token validation.
- **Flask** and **functions_framework** to define HTTP endpoints and handle requests.
It’s a fun and simple app to showcase serverless concepts and Firebase integration.

## Features

- **Sign Up**: Register a new user with email and password.
- **Sign In**: Sign in with Firebase ID Token.
- **Firebase Authentication**: Integrated Firebase Authentication service to securely manage users.
- **Serverless Deployment**: Deployed on **Google Cloud Run** using **Docker**.

## Prerequisites

Before running the application, make sure you have the following:

- **Google Cloud Account**: To use Google Cloud Run and Firebase services.
- **Firebase Project**: Set up Firebase and enable Firebase Authentication in your project.
- **Service Account Key**: Download the Firebase Admin SDK service account key (JSON format).
- **Docker**: To containerize and deploy the application to Cloud Run.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/abdougui/Firebase-Authentication-Serverless-Application.git
cd firebase-auth-serverless
```

### 2. Install Dependencies

Create a virtual environment and install the necessary dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Setup Firebase Admin SDK

- Create a Firebase Project on [Firebase Console](https://console.firebase.google.com/).
- Enable Firebase Authentication and configure it for Email/Password sign-in.
- Download the **service account key** (JSON file) and add it to the project folder.

### 4. Configure the Service Account Key Path

Make sure to update the path to the service account key in the `main.py` file:

```python
auth_service = AuthService(credentials_path="path/to/serviceAccountKey.json")
```
### 5. Deploy to Google Cloud Run
```bash

functions-framework --target=user_handler --port=ANY_AVAILABLE_PORT
```

### 6. Deploy to Google Cloud Run

Deploy the application to **Google Cloud Run**:

```bash
gcloud functions deploy user_handler \
--gen2 \
--region=europe-west1 \
--runtime=python312 \
--entry-point=YOUR_CODE_ENTRYPOINT \
--trigger-http
```

Replace `[YOUR_REGION]` with your Google Cloud region.
Replace `[YOUR_CODE_ENTRYPOINT]` with the name that you want on Google Cloud.

## Endpoints

Once deployed, the Cloud Run service provides the following endpoints:

### 1. **Sign Up**

- **POST** `/signup`
- **Request Body**:
  ```json
  {
    "email": "test@example.com",
    "password": "Test1234"
  }
  ```
- **Response**: A message indicating that the user was successfully created.
  
### 2. **Sign In**

- **POST** `/signin`
- **Request Body**:
  ```json
  {
    "id_token": "YOUR_FIREBASE_ID_TOKEN"
  }
  ```
- **Response**: Returns user details or an error message based on the token validation.

## Running Unit Tests

The project uses **unittest** for testing the serverless functions.

To run the tests, execute the following command:

```bash
python -m unittest discover -s tests
```

This will run all the tests located in the `tests/` directory.

## Contribution

Feel free to fork this project, open issues, or submit pull requests for improvements or feature requests!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Conclusion

The `README.md` provides a detailed description of the sample serverless application, guiding users through the setup, deployment, and usage of the Firebase Authentication system with Google Cloud Run. This should give users enough context to understand the project, set it up, and run it successfully.