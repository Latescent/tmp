from datetime import timedelta

from shared.helpers import now_iran, generate_token, generate_token_hash


class AccessToken:
    def __init__(self, user_id: int, token: str, **kwargs):
        self.user_id = user_id
        self.token = token
        self.plain_text_token = kwargs.get('plain_text_token')
        self.expires_at = now_iran() + timedelta(days=30)

    @classmethod
    def create(cls, user_id: int) -> 'AccessToken':
        token = generate_token()
        return cls(user_id, generate_token_hash(token), plain_text_token=token)

    def __str__(self):
        return self.plain_text_token
