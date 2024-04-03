"""Example of using lru_cache"""

from crypt import crypt

# TODO: Keep in secure place
salt = '$6$sqUw2lbtHTX6vfz0'

# TODO: Calculate once and store in database
users = {
    crypt('bunny', salt): 'bugs',
    crypt('duck', salt): 'daffy',
    crypt('fudd', salt): 'elmer',
}


def user_from_key(key):
    enc_key = crypt(key, salt)
    return users.get(enc_key)
