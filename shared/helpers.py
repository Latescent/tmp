from datetime import datetime
from zoneinfo import ZoneInfo
import secrets
import hashlib
import random
import string
from config import config
from domain.value_objects.mobile_number import MobileNumber


def now_iran():
    return datetime.now(ZoneInfo("Asia/Tehran"))


def get_referral_short_link(referral_code: str) -> str:
    return config.referral_host + '/' + referral_code


def generate_referral_code(length=6) -> str:
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def generate_token():
    token_secret = secrets.token_hex(40)
    plain_text_token = f"{token_secret}"
    return plain_text_token


def generate_token_hash(plain_text_token: str):
    return hashlib.sha256(plain_text_token.encode()).hexdigest()


def mask_mobile_number(mobile: MobileNumber) -> str:
    value = str(mobile)
    return "0" + value[:3] + "****" + value[-3:]


def mobile_normalize(mobile_number: str) -> str:
    return mobile_number[-10:]
