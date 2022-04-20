from timer import timed

def square_mult(base, exp, mod=None):
    n = 1
    for bit in bin(exp)[2:]:
        n *= n 
        n = n if mod is None else n % mod
        if bit == "1":
            n *= base
            n = n if mod is None else n % mod   
    return n
    
def fact(n):
    output = 1
    for i in range(1, int(n) + 1):
        output *= i
    return output

def calc_e():
    output = 0
    for i in range(18):
        output += (1 / fact(i))
    return output

@timed
def chudnovsky(digits):
    output = Decimal(0)
    for i in range(digits):
        numerator = ((-1) ** i) * (fact(6 * i)) * (545140134 * i + 13591409)  
        denominator = fact(2 * i) * (fact(i) ** 3) * 640320 ** (3 * i + 1.5)
        output += (Decimal(numerator) / Decimal(denominator))
    return round(1 / (12 * output), digits)

def hcf(i, j):
    rem = i % j
    while rem != 0:
        i = j
        j = rem 
        rem = i % j
    return j

def modinv(a, m):
    mod = m
    x, y = 1, 0
    if (m == 1):
        return 0
    while (a > 1):
        q = a // m 
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    return x % mod