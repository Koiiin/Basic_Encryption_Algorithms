from Crypto.PublicKey import RSA

file = open('Crypto/DATA_FORMATS/CERTainly_not/2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der', 'rb')
# rb: read binary
# 'rb' means that the file will be opened in read mode for binary data, 
# which is appropriate for working with binary files like cryptographic certificates.
modulus = RSA.importKey(file.read())


# modulus INTEGER, — n
print(modulus.n)