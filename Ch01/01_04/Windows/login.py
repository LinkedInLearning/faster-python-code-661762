"""Example login code"""
from bcrypt import hashpw as crypt
import sqlite3

salt = b'$2b$12$dUJI8FM2kJC0BzMdNspgQe'  # Bad security, store safely
db = sqlite3.connect('passwords.db')
db.row_factory = sqlite3.Row  # Access columns by names


def user_passwd(user):
    """Get user password from db"""
    cur = db.cursor()
    cur.execute('SELECT passwd FROM users WHERE user = ?', (user, ))
    row = cur.fetchone()
    if row is None:  # No such user
        raise KeyError(user)
    return row['passwd']


def encrypt_passwd(passwd):
    """Encrypt user password"""
    return crypt(passwd, salt)


def login(user, password):
    """Return True is user/password pair matches"""
    try:
        db_passwd = user_passwd(user)
    except KeyError:
        return False

    passwd = encrypt_passwd(password.encode('utf-8'))
    return passwd == db_passwd
