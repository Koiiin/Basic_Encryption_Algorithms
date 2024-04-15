def gcd(a, b):
    if (a == 0 or b == 0):
        return a+b
    while (a != b):
        if (a > b):
            a -= b
        elif (b > a):
            b -= a
    return a

a = 66528
b = 52920
print (gcd(a, b))