from functools import lru_cache
@lru_cache(None)
def isPrime(n):
    if n%2==0:
        return False
    for i in range(3,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


primes = set()
for i in range(3, 10**6, 2):
    if isPrime(i):
        primes.add(i)

print(primes)
