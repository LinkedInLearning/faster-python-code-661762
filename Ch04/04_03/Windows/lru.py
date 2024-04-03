"""Example of using lru_cache"""

from bcrypt import hashpw as crypt
from functools import lru_cache

# TODO: Keep in secure place
salt = b'$2b$12$dUJI8FM2kJC0BzMdNspgQe'

# TODO: Calculate once and store in database
users = {
    crypt(b'bunny', salt): 'bugs',
    crypt(b'duck', salt): 'daffy',
    crypt(b'fudd', salt): 'elmer',
}


@lru_cache(maxsize=1024)
def user_from_key(key):
    enc_key = crypt(key.encode('utf-8'), salt)
    return users.get(enc_key)
