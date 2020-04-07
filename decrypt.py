from Crypto.Util.number import *
from Crypto.PublicKey import *
import gmpy2
c = "44e66fa36292bcfc3cce5ca922459594b6f83e8e6e8d60a9091b05172b1c622a5bb8f83a8d735d9500be5a9b12d28f3ba4f2b77e44db17790e048d9c047d051dceaffd849edbfd2a8d49655270b1f9dc9101e5460e0b5dd499a2883d834be9273cc9be63897affc3121a16b4236b09f40df7a62aeeea8b1ce01bd5f8a14f77df".decode('hex')
ct = bytes_to_long(c)
n = 113688948285842899107975301022215849433130338840548967469541502266648698859427789882909935207845403124414725514641333266767452747358231793289531990179230714791473631866452291072856425388757401443749925740001136871466483114739269309310921145831373531460767011787628854371542639519059269733470587037962830964359
e = 65537
s = 11037042649783145182273307936666186066672869833902665306938737534685880312248250406172058334270104093094118712601752738987028280488106705463344104383358960137505365749881811031713020908366310747455165631530131553809081551583619903892751314809459201354290153163772
#According to the encrypt.py
#To solve this challenge we need to understand Fermat Little Theorem
#pow(a,p) = a (mod p) 
#s = pow(2, p - 0xdeadbeef, n)  ==> s = pow(2, p - 0xdeadbeef) (mod n)
#Let t = 0xdeadbeef
# s = k*n + pow(2, p - t)
# s = k*n + (pow(2,p) * pow(2,-t))
# s = k*p*q + (pow(2,p) * pow(2,-t))        {Since, n = p*q}
#Apply (pow(2,t) mod p) on both sides
# (pow(2,t) mod p)*s = 0 + (pow(2,p) mod p)  {Since, When k*p*q is divided by p then remainder is 0}
# We know that, pow(2,p) (mod p) = kp + 2
# pow(2,p)(mod p) - 2 = kp ==> pow(2,p,p) - 2 = kp
# pow(2,t)*s - 2 = kp
# So, p = GCD(kp,n)

kp = (pow(2,0xdeadbeef)*s)-2
p = GCD(kp,n)
q = n/p
phin = (p-1)*(q-1)
d = inverse(e,phin)
m = pow(ct,d,n)
flag = long_to_bytes(m)
print flag
