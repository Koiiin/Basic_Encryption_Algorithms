str = 'label'
flag = 'crypto{'
for ch in str:
    flag += chr(ord(ch)^13)
flag += '}'
print(flag)

#crypto{aloha}