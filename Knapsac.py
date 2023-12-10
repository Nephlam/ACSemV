import math

def getknap(key,n,m):
    vals = key.split(',')
    k=""
    for i in vals:
        ans = (int(i)*int(n))%int(m)
        if k=="":
            k= k +str(ans)
        else:
            k= k + ","+str(ans)
    return k


def getcipher(publickey, data):
    vals = publickey.split(',')
    weight = [int(v) for v in vals]
    total = 0

    for i in range(len(weight)):
        if data[i]=='1':
            total = total + weight[i]
    
    return total

size = int(input("Enter the size of your message: "))
data = input(f"Enter your {size} bit message: ")
priv = input("Enter the private key in Super Inc Seq. (separated by comma): ")

sum=0
for i in priv.split(','):
    sum = sum + int(i)
a= 10 - (sum%10)
m=sum+a
print("Value of m: ",m)

i=2
while True:
    ans = math.gcd(i,m)
    if(ans ==1):
        break
    i=i+1
n=i
print(f"Corresponding value of n for m = {m} is:", n)

pubkey = getknap(priv,str(n),str(m))
print("Public key: ",pubkey)

if size==4:
    cipher = getcipher(pubkey,data)
    print("Cipher is:", cipher)

else:
    data1=data[:4]
    data2=data[4:]
    cipher1 = getcipher(pubkey,data1)
    cipher2 = getcipher(pubkey,data2)
    print("Ciphertest is :",str(cipher1)+str(cipher2))


