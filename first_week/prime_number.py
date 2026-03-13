#  created a function check prime
def is_prime(n):
    if n < 2:
        return False    
    for i in range(2, n):
        if n % i == 0:
            return False  
    return True
primes = [x for x in range(11) if is_prime(x)]
print(primes)
