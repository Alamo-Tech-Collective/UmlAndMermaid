from typing import Optional
import secrets
import time


class Session:
    def __init__(self, token: Optional[str] = None):
        self._token = token or secrets.token_urlsafe(32)
        self._created_at = time.time()
        self._expiry_duration = 3600  # 1 hour in seconds

    @classmethod
    def create(cls, user: 'User') -> 'Session':
        if not user:
            raise ValueError("User cannot be None")
        return cls()

    def is_valid(self) -> bool:
        current_time = time.time()
        elapsed_time = current_time - self._created_at
        return elapsed_time < self._expiry_duration

    @property
    def token(self) -> str:
        return self._token