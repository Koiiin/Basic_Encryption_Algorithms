def euclid(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = euclid(b % a, a)
        return gcd, y - (b // a) * x, x

a = 26513
b = 32321
print(euclid(a, b))

#(1, 10245, -8404)