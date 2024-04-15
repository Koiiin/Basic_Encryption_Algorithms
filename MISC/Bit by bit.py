from Crypto.Util.number import long_to_bytes

flag = ''
q = 117477667918738952579183719876352811442282667176975299658506388983916794266542270944999203435163206062215810775822922421123910464455461286519153688505926472313006014806485076205663018026742480181999336912300022514436004673587192018846621666145334296696433207116469994110066128730623149834083870252895489152123
with open('output.txt') as f:
    dong = f.readlines()
    for i in range(1, len(dong), 2):
        (c1, c2) = dong[i].strip().split(',')
        c1 = int(c1.split('=')[1], 16)
        c2 = int(c2.split('=')[1][:-1], 16)
        if (pow(c2, (q - 1)//2, q) == 1):
            flag = '1' + flag
        else:
            flag = '0' + flag
print(long_to_bytes(int(flag, 2)))

#crypto{s0m3_th1ng5_4r3_pr3served_4ft3r_encrypti0n}