from pwn import *

n = 531137992816767098689588206552468627329593117727031923199444138200403559860852242739162502265229285668889329486246501015346579337652707239409519978766587351943831270835393219031728127
r = remote('185.172.165.118', 4008, level = 'info')
s = []
print('receiving data')
for _ in range(3):
 r.sendafter(b'> ',b'1')
 s.append(int(r.recvline()))
print('data received')
def crack_incr(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return modulus, multiplier, increment

def crack(states, modulus):
    multiplier = (states[2] - states[1]) * pow(states[1] - states[0], -1, modulus) % modulus
    return crack_incr(states, modulus, multiplier)

print('cracking')
n, m, c = crack(s, n)
print('cracked, sending')
r.sendafter(b'> ', b'2')

next = (s[-1]*m+c)%n

r.sendafter(b'> ', str(next).encode())
print("flag received: " + r.recvline().decode()[:-1])

r.close()
