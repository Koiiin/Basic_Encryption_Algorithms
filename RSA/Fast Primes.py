from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse

public = RSA.importKey(open('key.pem').read())
n = int(public.n)
e = int(public.e)
print(n)
print(e)
e=65537
n=4013610727845242593703438523892210066915884608065890652809524328518978287424865087812690502446831525755541263621651398962044653615723751218715649008058509
p=51894141255108267693828471848483688186015845988173648228318286999011443419469
q=77342270837753916396402614215980760127245056504361515489809293852222206596161

phi = (p - 1) * (q - 1)
d = inverse(e, phi)
c = open("cipher.txt", 'r').read()
key = RSA.construct((n, e, d))
cipher = PKCS1_OAEP.new(key)
decrypt = cipher.decrypt(bytes.fromhex(c))
print(decrypt)

#crypto{p00R_3570n14}