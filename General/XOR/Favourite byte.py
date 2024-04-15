from pwn import xor

str = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
for i in range(256):
    flag = xor(str,i).decode('utf-8')
    if "crypto" in flag:
        print(flag)
        exit

#crypto{0x10_15_my_f4v0ur173_by7e}