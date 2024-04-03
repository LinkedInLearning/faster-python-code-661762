"""Example of using lru_cache"""

from crypt import crypt
from functools import lru_cache

# TODO: Keep in secure place
salt = '$6$sqUw2lbtHTX6vfz0'

# TODO: Calculate once and store in database
users = {
    crypt('bunny', salt): 'bugs',
    crypt('duck', salt): 'daffy',
    crypt('fudd', salt): 'elmer',
}


@lru_cache(maxsize=1024)
def user_from_key(key):
    enc_key = crypt(key, salt)
    return users.get(enc_key)
