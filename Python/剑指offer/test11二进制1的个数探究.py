i = 0xffffffff
n = 3
m = -3

def intToBin32(i):
    return (bin(((1 << 32) - 1) & i)[2:]).zfill(32)

print(bin(n))
print(bin(m&0xffffffff))
print(intToBin32(m))

for i in range(n):
    print(i)

for i in range(1,n):
    print(i)