import hashlib
import os
import jwt
from datetime import datetime, timedelta

# Importing shared dependencies
from security.encryption import encryptData
from security.compliance.gdpr import complyWithGDPR

# Constants
SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# User schema for reference
class User:
    def __init__(self, username, email, password_hash):
        self.username = username
        self.email = email
        self.password_hash = password_hash

# Authentication functions
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return hash_password(plain_password) == hashed_password

def authenticate_user(user: User, password: str) -> bool:
    return verify_password(password, user.password_hash)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload if payload['exp'] >= datetime.utcnow() else None
    except jwt.PyJWTError:
        return None

# Example usage
if __name__ == "__main__":
    # Assume we have a user object from the database
    user = User('john_doe', 'john@example.com', hash_password('securepassword123'))
    
    # Authenticate the user
    if authenticate_user(user, 'securepassword123'):
        # Create token
        access_token = create_access_token(data={"sub": user.username})
        print(f"Access Token: {access_token}")
    else:
        print("Authentication failed")

    # Decode the token
    user_data = decode_access_token(access_token)
    if user_data:
        print(f"User {user_data['sub']} has been successfully authenticated")
    else:
        print("Invalid or expired token")