
from math import gcd, lcm
from operator import mod
import random

#Prime numbers
P  = 61
Q = 53
#the function is_prime was taken from the following  link:
#https://en.wikipedia.org/wiki/Primality_test#Frobenius_primality_test
def is_prime(n) :
    if n <= 3:
        return n > 1
    if not n%2 or not n%3:
        return False
    i = 5
    stop = int(n**0.5)
    while i <= stop:
        if not n%i or not n%(i + 2):
            return False
        i += 6
    return True

def are_coprime(e,phi):
    if(gcd(e,phi)==1):return True
    return False


def totient (p,q):
    return lcm(p-1,q-1)

def public_key(phi):
    random_e = random.randint(2,phi-1)

    while(True):
        if(are_coprime(random_e,phi)) and (phi%random_e!=0) and (is_prime(random_e)):
            break
        else:
            random_e = random.randint(0,phi)
           
            
    return random_e
   
def private_key(e,phi):
    random_d = random.randint(0,10000)
    while(not(mod(random_d*e,phi)==1)):
            random_d = random.randint(0,10000)
        
    return random_d


def encrypt(text,n,e):
    text  =list(text)
    c= lambda m: (ord(m)**e)%n
    encrypt_text = list(map(c,text))
    
    return encrypt_text


def decrypt(encrypt_text,n,d):
    m= lambda c: (c**d)%n
    decrypt_text_num = list(map(m,encrypt_text))
    decrypt_text_str  = ''.join(list(map(chr,decrypt_text_num)))

    return decrypt_text_str

def main():
    n = P *Q
    phi = totient(P,Q)
    e = public_key(phi) 
    d = private_key(e,phi)

    text = input('Enter with a text :')
    
    print()
    print('public_key :' + str(e))
    print('private_key :' + str(d))

    encrypt_text = encrypt(text,n,e)
    decrypt_text = decrypt(encrypt_text,n,d)

    print()

    print('Ecnrypt :',end='')
    print(encrypt_text)
    print('decrypt : ' + decrypt_text)
   
   

main()

