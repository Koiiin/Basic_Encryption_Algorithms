from Crypto.PublicKey import RSA

# The "ssh-keygen" command is used to produce these public-private keypairs.

file = open('Crypto/DATA_FORMATS/SSH_Keys/bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub', 'r')

modulus_n = RSA.importKey(file.read())

print(modulus_n.n)