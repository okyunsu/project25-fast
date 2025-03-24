from enum import Enum


class LoginAction(Enum):
    LOGIN = "login"
    LOGOUT = "logout"
    VERIFY_TOKEN = "verify_token"
