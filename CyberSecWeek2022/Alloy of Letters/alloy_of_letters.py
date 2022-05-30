
# get ciphered contents
f = open("flag.txt")
s=""
for i in f.readlines():
    s+=i

tmp = ""
offset = 1

#try different offsets and look for the CTFUA templates
while('CTFUA{' not in tmp):
    tmp = ""
    for i in s:
        tmp += chr((ord(i)+offset)%127)
    offset +=1


print(tmp)

print(offset)