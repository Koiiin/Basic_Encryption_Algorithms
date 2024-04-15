from Crypto.PublicKey import RSA

file = open('Crypto/DATA_FORMATS/Transparency/transparency_afff0345c6f99bf80eab5895458d8eab.pem', 'r')

flag = RSA.importKey(file.read())

# Searching google about finding the subdomain 
# then found out a website that search for certificates of a domain
# https://crt.sh/?q=cryptohack.org

# Found this: thetransparencyflagishere.cryptohack.org
# Flag: crypto{thx_redpwn_for_inspiration}