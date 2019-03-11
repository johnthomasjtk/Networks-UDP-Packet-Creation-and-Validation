import sys
import hashlib
import math
hd = sys.argv[1]
s_ip = sys.argv[2]
d_ip = sys.argv[3]
s_port = hd[0:4]
d_port = hd[4:8]
checksum = hd[12:16]
length = hd[8:12]
data = hd[16:]
d1 = data
sp = int(s_port, 16)
dp = int(d_port, 16)
q = int(length, 16)
tlen = ((len(d1)*4)/8)+8
if tlen == q:
    a = '.' .join(format(int(x), '08b') for x in s_ip.split('.'))
    b = '.' .join(format(int(x), '08b') for x in d_ip.split('.'))
    c = a.split(".")
    d = b.split(".")
    sourceadd1 = c[0] + c[1]
    sourceadd2 = c[2] + c[3]
    destinationaddr1 = d[0] + d[1]
    destinationaddr2 = d[2] + d[3]
    sourceadd1 = int(sourceadd1,2)
    sourceadd2 = int(sourceadd2,2)
    destinationaddr1 = int(destinationaddr1,2)
    destinationaddr2 = int(destinationaddr2,2)
    dlen=len(data)
    while (dlen%4) != 0:
                dlen += 1
                data += "0"
    n = 4
    data1 = [int(data[i:i+n],16) for i in range(0, len(data), n)]
    sum  = sourceadd1 + sourceadd2 + destinationaddr1 + destinationaddr2 + int(sp) + int(dp)
    for i in range (len(data1)):
        sum += data1[i]
    tlen = ((len(d1)*4)/8)+8
    protocol = 17
    sum = sum + protocol + tlen + tlen
    totsum = hex(sum)[2:]
    x = len(totsum) - 4
    jk =""
    for i in range (x,len(totsum)):
        jk+=totsum[i]
    kj =""
    for i in range (x):
        kj+=totsum[i]
    s = int(jk,16)
    v = int(kj,16)
    sum1 = s + v
    f = hex(sum1)
    w = f[2:]
    g = bin(int(w,16))[2:].zfill(16)
    ib_string = ""
    for bit in g:
        if bit == "1":
            ib_string += "0"
        else:
            ib_string += "1"
    t = hex(int(ib_string,2))[2:]
    t=t.zfill(4)
    if t == checksum:
        print sp
        print dp
        print tlen
        print "0x"+t
        sha=""
        for i in range(0,len(d1),2):
            r = d1[i:i+2]
            r1 = int(r,16)
            r=chr(int(r1))
            sha+=r
            sha1=hashlib.sha256(sha).hexdigest()
        print sha1
    else:
        print "Invalid UDP segment"
else:
    print "Invalid UDP segment"
