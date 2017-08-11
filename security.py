#all security
from passlib.hash import pbkdf2_sha256


def encrypt_password(raw_password):
	hash = pbkdf2_sha256.hash(raw_password)
	return hash


def verify_password(raw_password, encrypted_password):
	return pbkdf2_sha256.verify(raw_password, encrypted_password)


