from functools import reduce
from gmpy2 import gcd,gcdext,invert

def crack_unknown_increment(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return int(modulus), int(multiplier), int(increment)

def crack_unknown_multiplier(states, modulus):
    multiplier = (states[2] - states[1]) * invert(states[1] - states[0], modulus) % modulus
    return crack_unknown_increment(states, modulus, multiplier)
#def crack_lcg(seeds):
 #   a = ((seeds[2] - seeds[1]) * invert(seeds[1] - seeds[0], n)) % n 
  #  return a, (seeds[1] - seeds[0]*a) % n
def crack_unknown_modulus(states):
    diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
    zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
    modulus = abs(reduce(gcd, zeroes))
    print(crack_unknown_multiplier(states, modulus))
    return None
n = 9444729917070668893
flag = "FwordCTF{"
output = [6680465291011788243, 5100570103593250421, 5906808313299165060, 1965917782737693358, 9056785591048864624, 1829758495155458576, 6790868899161600055, 1596515234863242823, 1542626304251881891, 8104506805098882719, 1007224930233032567, 3734079115803760073, 7849173324645439452, 8732100672289854567, 5175836768003400781, 1424151033239111460, 1199105222454059911, 1664215650827157105, 9008386209424299800, 484211781780518254, 2512932525834758909, 270126439443651096, 3183206577049996011, 3279047721488346724, 3454276445316959481, 2818682432513461896, 1198230090827197024, 6998819122186572678, 9203565046169681246, 2238598386754583423, 467098371562174956, 5653529053698720276, 2015452976526330232, 2551998512666399199, 7069788985925185031, 5960242873564733830, 8674335448210427234, 8831855692621741517, 6943582577462564728, 2159276184039111694, 8688468346396385461, 440650407436900405, 6995840816131325250, 4637034747767556143, 3074066864500201630, 3089580429060692934, 2636919931902761401, 5048459994558771200, 6575450200614822046, 666932631675155892, 3355067815387388102, 3494943856508019168, 3208598838604422062, 1651654978658074504, 1031697828323732832, 3522460087077276636, 6871524519121580258, 6523448658792083486, 127306226106122213, 147467006327822722, 3241736541061054362, 8781435214433157730, 7267936298215752831, 3411059229428517472, 6597995245035183751, 1256684894889830824, 6272257692365676430, 303437276610446361, 8730871523914292433, 6472487383860532571,5022165523149187811, 4462701447753878703, 1590013093628585660, 4874224067795612706]  
X = []
for i in range(len(flag)):
    X.append(ord(flag[i])^output[i])
crack_unknown_modulus(X)
n = 9444729917070668893
m = 7762244320486225184
c = 731234830430177597
for i in range(1,len(X)):
	assert X[i] == (X[i-1]*m + c) % n
s = []
s.append(X[0])
for i in range(1,len(output)):
	s.append((s[i-1]*m + c)%n)
flag = ""
for i in range(len(output)):
	flag+= chr(s[i]^output[i])
print("[+] Flag: ",flag)

