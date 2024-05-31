n = int(input("Enter a Number->"))
r = ""
ns = ""
# number to binary
while(n>0):
    r = str(n%2)
    ns = r + ns
    n = n // 2

# check it is 8 bit if not then add 0 in start position
if len(ns)!= 8:
    ns = "0"*(8-len(ns)) + ns
print(ns)

# create 2 strings s1 and s2 for 4 bites
s1 = ns[:4]
s2 = ns[4:]

print(s1)
print(s2)

# add s2 then s1 in ns
ns = int(s2 + s1)
print(ns)

# converrt ns(binary) to decimal
power = 0
sump = 0
while(ns>0):
    rem = ns % 10
    sump += rem*pow(2,power)
    ns = ns//10
    power += 1
print(sump)



input - 100
output - 70
