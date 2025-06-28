import os
import base64
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

load_dotenv()

# key path
SERVICE_KEY_PATH = "service-key.json"
firebase_key_b64 = os.getenv("FIREBASE_KEY_B64")

# decode b64 key
if firebase_key_b64:
    if not os.path.exists(SERVICE_KEY_PATH):
        with open(SERVICE_KEY_PATH, "wb") as f:
            f.write(base64.b64decode(firebase_key_b64))
else:
    key_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", SERVICE_KEY_PATH)
    if not os.path.exists(key_path):
        raise FileNotFoundError(f"Service key not found at {key_path}")

# initialize firebase app
try:
    firebase_admin.get_app()
except ValueError:
    cred = credentials.Certificate(SERVICE_KEY_PATH)
    firebase_admin.initialize_app(cred)

# firestore client
db = firestore.client()