s = input("Enter a String ->")
alpha = "abcdefghijklmnopqrstuvwxyz"
x = 0 
y = 0
# for find freq of each char
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

for k,f in d.items():
    # i = index of k in alpha
    i = alpha.index(k) + 1
    if i%2==0 and f%2==0 or i%2!=0 and f%2!=0: #i,f dono ya toh odd ya even
        # agar i + f odd ho toh x -> x + 1
        if (i + f) % 2 != 0:
            x += 1
        # agar i + f even ho toh y -> y + 1
        else:
            y += 1

# if x + y odd ho toh
if (x+y)%2 !=0:
    print("Odd")
else:
    print("Even")

# Input: 
# s = "abbbcc"
# Output: 
# ODD
# Explanation: 
# # x = 0 and y = 1 so (x + y) is ODD. 'a' occupies 1st place(odd) in english alphabets and its frequency is odd(1), 'b' occupies 2nd place(even) but its frequency is odd(3) so it doesn't get counted and 'c' occupies 3rd place(odd) but its frequency is even(2) so it also doesn't get counted.
# Input: 
# s = "nobitaa"
# Output: 
# EVEN
# Explanation: 
# # x = 0 and y = 2 so (x + y) is EVEN.           