import hashlib
from config import storage, secret_key
import jwt


def hash_md5(data):
    return hashlib.md5(data.encode('utf-8')).hexdigest()


def registrate(account):
    result = {
        "error": True,
        "message": "User already exists."
    }
    account['password'] = hash_md5(account.get('password'))
    email = account.get("email")
    storage_account = storage.get_by_email(email)
    if storage_account is None:
        storage.add(account)
        result = {
            'error': False,
            'message': "OK!"
        }
    return result


def login(account):
    email = account.get("email")
    data = storage.get_by_email(email)
    password = hash_md5(account.get("password"))
    saved_password = data.get("password")
    if password == saved_password:
        return make_jwt(data)
        

def make_jwt(data):
    return jwt.encode(data, secret_key, algorithm='HS256')