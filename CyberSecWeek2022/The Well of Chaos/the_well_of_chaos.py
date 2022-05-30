# get ciphered contents
f = open("flag.txt")
s=""
for i in f.readlines():
    s+=i

res  = ""


while(s):
    res += s[2]+s[0]+s[3]+s[1]
    s = s[4:]

print(res)