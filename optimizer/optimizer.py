from pwn import *
import json, codecs

r = remote('45.134.3.200', 9660)#, level = 'debug')

r.recvline()
r.recvline()

print('starting hanoi')

i = r.recvline()
while(not i.startswith(b"level 2")):
 l = len(json.loads(i))
 r.sendline(str(2**l-1).encode())
 r.recvuntil(' ')
 i = r.recvline()

print('done hanoi')

 # l = len(json.loads(r.recvline()))
 # r.sendline(str(2**l-1).encode())
 # r.recvuntil(' ')
 # r.recvline()

from merge import mergeSort
print('starting merge sort')
i = r.recvline()
while(not i.startswith(b"you won")):
 l = json.loads(i)
 r.sendline(str(mergeSort(l, len(l))).encode())
 r.recvuntil(' ')
 i = r.recvline()

print('done merge sort')

print(i.decode()[:-1])
r.close()