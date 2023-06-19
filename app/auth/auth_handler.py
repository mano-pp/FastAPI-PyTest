import time
import os
from dotenv import load_dotenv
from typing import Dict
import jwt

load_dotenv(dotenv_path=".env")

JWT_SECRET = os.environ["secret"]
JWT_ALGORITHM = os.environ["algorithm"]

def token_response(token: str):
    return {
        "access_token": token
    }

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}

def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)
