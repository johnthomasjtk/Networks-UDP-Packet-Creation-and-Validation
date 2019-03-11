import sys
ipsa=sys.argv[1]
port1=sys.argv[2]
ipda=sys.argv[3]
port2=sys.argv[4]
data=sys.argv[5]
ptcl=17
l=[]
a=[]
l=ipsa.split('.')
for i in l:
   i=bin(int(i))[2:].zfill(8)
   a.append(i)
m=a[0]+a[1]
n=a[2]+a[3]
p1=int(m,2)+int(n,2)
first=[]
second=[]
first=ipda.split('.')
for j in first:
   j=bin(int(j))[2:].zfill(8)
   second.append(j)
t=second[0]+second[1]
u=second[2]+second[3]
p2=int(t,2)+int(u,2)
d=data
l1=len(data)
len1=l1 * 4
len2=len1%16
len3=len1/8
second=[]
first=ipda.split('.')
total_len = len3+8
#print total_len
h3=hex(total_len)[2:].zfill(4)
while (l1%4) != 0:
            l1 += 1
            d += "0"
n = 4
d1 = [int(d[i:i+n],16) for i in range(0, len(d), n)]
s1  = p1+p2+ int(port1) + int(port2)
for i in range (len(d1)):
    s1 += d1[i]
s1=s1+ptcl+total_len+total_len
rsum=hex(s1)[2:]
m = len(rsum) - 4
tmp1=""
for i in range (m,len(rsum)):
    tmp1+=rsum[i]
tmp2=""
for i in range (m):
    tmp2+=rsum[i]
s = int(tmp1,16)
v = int(tmp2,16)
s1 = s + v
f = hex(s1)
w = f[2:]
g = bin(int(w,16))[2:].zfill(16)
carry = ""
for bit in g:
    if bit == "1":
        carry += "0"
    else:
        carry += "1"
t = hex(int(carry,2))
checksum=t[2:]
srp=int(port1)
srcp=  hex(srp)[2:]
dp=int(port2)
destp=hex(dp)[2:]
z=""
z=srcp+destp+h3+checksum+data
print z
