import secrets
import string
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def generate_api_key(key_length=32):
    character_set = string.ascii_letters + string.digits
    api_key = ''.join(secrets.choice(character_set) for _ in range(key_length))
    return api_key

def hashed_password(plain_password):
    return hash(plain_password)

def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)