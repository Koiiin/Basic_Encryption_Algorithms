from Crypto.PublicKey import RSA

file = open('Crypto/DATA_FORMATS/Privacy-Enhanced_Mail/privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem', 'r')
# r: This stands for "read mode," 
# which means that the file will be opened for reading. You can read data from the file, but you cannot write to it or modify its contents.

# The RSA.importKey() return an RsaKey object. 
# The private key is the 'd' properties of RsaKey

key = RSA.importKey(file.read())
# print(key.n)
# print(key.e)

# RSAPrivateKey ::= SEQUENCE {
# version Version,
# modulus INTEGER, — n
# publicExponent INTEGER, — e
# privateExponent INTEGER, — d #
# prime1 INTEGER, — p
# prime2 INTEGER, — q
# exponent1 INTEGER, — d mod (p-1)
# exponent2 INTEGER, — d mod (q-1)
# coefficient INTEGER, — (inverse of q) mod p
# otherPrimeInfos OtherPrimeInfos OPTIONAL

print(key.d)