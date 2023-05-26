from crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

message = b'You can attack now!'
key = RSA.importKey(b'win')
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(message)
