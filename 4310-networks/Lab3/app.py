p0m=0b1111100000000000
p1m=0b0000011111110000
p2m=0b1100011110001110
p3m=0b0011011001101101
p4m=0b1010110101011011

a=0b1010101010101001

print('a'+bin(a))

p0=p0m&a
p1=p1m&a
p2=p2m&a
p3=p3m&a
p4=p4m&a

def parityOf(int_type):
    parity = 0
    while (int_type):
        parity = ~parity
        int_type = int_type & (int_type - 1)
    return(parity)

if (parityOf(p0)==-1):
	a = (a << 1) + 0b1
else:
	a = (a << 1) + 0b0

print('Parity of p0: '+str(parityOf(p0))+'')
print('a'+bin(a)+'\n')

if (parityOf(p1)==-1):
	a = (a << 1) + 0b1
else:
	a = (a << 1) + 0b0

print('Parity of p1: '+str(parityOf(p1))+'')
print('a'+bin(a)+'\n')

if (parityOf(p2)==-1):
	a = (a << 1) + 0b1
else:
	a = (a << 1) + 0b0

print('Parity of p2: '+str(parityOf(p2))+'')
print('a'+bin(a)+'\n')

if (parityOf(p3)==-1):
	a = (a << 1) + 0b1
else:
	a = (a << 1) + 0b0

print('Parity of p3: '+str(parityOf(p3))+'')
print('a'+bin(a)+'\n')

if (parityOf(p4)==-1):
	a = (a << 1) + 0b1
else:
	a = (a << 1) + 0b0

print('Parity of p4: '+str(parityOf(p4))+'')
print('a'+bin(a)+'\n')