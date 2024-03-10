def gcd(a,b):
    assert int(a) == a and int(b) == b, "Please enter numaric entry"
    if a<0:
        a = -1 * a
    if b<0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
print(gcd(6,12))


# **GCD*********    *
#                   *      Euclidean algorithm
# gcd(8,12) = 4     *      *******************
#                   *     gcd(48,18)
# 8 = 2 * 2 * 2     *     step 1: 48/18 = 2 remainder 12
# 12 = 2 * 2 * 3    *     step 2: 18/12 = 2 remainder 6
#                   *     step 3: 12/6 = 2 remainder 0
#                   *    
#                   *     when remainder = 0 then GCD = base