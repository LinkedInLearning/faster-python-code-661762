"""Encrypt password with sha256 - checking another option"""

from login import salt

from hashlib import sha256

salt256 = salt.encode('utf-8')  # Convert to bytes


def encrypt_passwd2(passwd):
    """Encrypt password with sha256"""
    return sha256(passwd.encode('utf-8') + salt256).hexdigest()
