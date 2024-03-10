def sumOfDigit(n):
    assert n>=0 and int(n) == n, "Please enter numaric entry"
    if n==0:
        return 0
    else:
        return int(n%10) + sumOfDigit(int(n//10))
    
print(sumOfDigit(21))


# 21 => 2 + 1 = 3 