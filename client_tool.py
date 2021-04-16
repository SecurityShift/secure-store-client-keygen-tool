#!/usr/bin/env python
import nacl.utils
from nacl.public import PrivateKey
from nacl.encoding import Base64Encoder

API_KEY_LENGTH = 32

def generate_key_pair():
	private_key = PrivateKey.generate()
	return Base64Encoder.encode(bytes(private_key)).decode("UTF-8"), Base64Encoder.encode(bytes(private_key.public_key)).decode("UTF-8")

def generate_api_key():
	return Base64Encoder.encode(nacl.utils.random(API_KEY_LENGTH)).decode("UTF-8")

private_key, public_key = generate_key_pair()
api_key = generate_api_key()

print("Private Key: " + private_key)
print("Public Key: " + public_key)
print("API Key: " + api_key)

 
