from pwn import *
import json, codecs

r = remote('45.134.3.200', 9660, level = 'debug')

r.recvline()
r.recvline()

i = r.recvline()

while(not i.startswith(b"level 2")):
 l = len(json.loads(i))
 r.sendline(str(2**l-1).encode())
 r.recvuntil(' ')
 i = r.recvline()

 # l = len(json.loads(r.recvline()))
 # r.sendline(str(2**l-1).encode())
 # r.recvuntil(' ')
 # r.recvline()

r.close()