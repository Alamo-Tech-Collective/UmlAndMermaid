from typing import Optional
import hashlib


class User:
    def __init__(self, username: str, password: str):
        self._username = username
        self._password = self._hash_password(password)

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self, password: str) -> bool:
        hashed_input = self._hash_password(password)
        return self._password == hashed_input

    @property
    def username(self) -> str:
        return self._username