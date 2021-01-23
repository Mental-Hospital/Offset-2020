from pwn import *
import json, codecs

r = remote('45.134.3.200', 9660, level = 'debug')

r.recvline()
r.recvline()
l = len(set(json.loads(r.recvline())))
r.sendline(str(2**l-1).encode())
r.recvline()