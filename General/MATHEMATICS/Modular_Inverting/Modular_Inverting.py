# Using Fermat's little theorem
# In the case of a not divisible by p:
# a^(p-1) ≡ 1 mod p 
# <=> a^(p-1) % p = 1


#topic: 3 * d ≡ 1 mod 13

# a^(p-1) ≡ 1 mod p
# a^(p-1) * a^(-1) ≡ a^(-1) mod p
# a^(p-2) * a * a^(-1) ≡ a^(-1) mod p
# a^(p-2) ≡ a^(-1) mod p 
# <=>
# a^(p-2) % p = a^(-1) = d

a = 3
p = 13

print(pow(a, p-2, p))

