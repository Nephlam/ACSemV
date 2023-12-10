import random
import math

def findinv(i,totient):
    j=2 
    while j>1:
        if (i*j)%totient ==1:
            break
        j+=1
    return j

def encryption(plaintext, public_key):
    ciphertext = (plaintext**public_key[0])%public_key[1]
    return ciphertext

def decryption(ciphertext, private_key):
    plaintext = (ciphertext**private_key[0])%private_key[1]
    return plaintext
plaintext= int(input("Enter the plaintext:"))
p = int(input("Enter the prime number p:"))
q = int(input("Enter the prime number q:"))
n = p*q
totient = (p-1)*(q-1)
e = random.randrange(2,totient)

while math.gcd(e,totient)!=1:
    e = random.randrange(e,totient)
    
d = findinv(e,totient)

private_key=[d,n]
public_key=[e,n]

print("The public key is:",public_key)
print("The private key is:", private_key)

ciphertext = encryption(plaintext, public_key)
print("The cipher text is: ", ciphertext)
plain_text = decryption(ciphertext, private_key)
print("The plaintext after decryption is: ",plain_text)