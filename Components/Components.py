def gcd(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b :
        return gcd(a-b,b)
    return gcd(a,b-a)

def Inverst(a,m):
    m0 = m
    y = 0
    x = 1
    if m == 1:
        return 0
    while a > 1:
        q = a/m
        t = m
        m = a % m
        a = t
        t = y
        y =x - q * y
        x = t
    if x < 0:
        x += m0
    return int(x)



def bpvn(base, exp, n):
    t = 1
    while exp > 0:
        if exp % 2 != 0:
            t = (t * base) % n
        base = (base * base) % n
        exp = int(exp / 2)
    return t % n
