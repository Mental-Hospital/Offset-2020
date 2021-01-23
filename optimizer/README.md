# Optimizer
Fun problem, don't want to do it again.
We used `pwnlib` in Python 3.
## Hanoi
The hanoi section turned out to just be `2^(length of list)-1`:
```python
i = r.recvline()
while(not i.startswith(b"level 2")):
 l = len(json.loads(i))
 r.sendline(str(2**l-1).encode())
 r.recvuntil(' ')
 i = r.recvline()
```
It just keeps going until level two begins.
## Merge Sort
We used a merge sort inversion counter found [here](https://www.geeksforgeeks.org/counting-inversions/).
```python
from merge import mergeSort
print('starting merge sort')
i = r.recvline()
while(not i.startswith(b"you won")):
 l = json.loads(i)
 r.sendline(str(mergeSort(l, len(l))).encode())
 r.recvuntil(' ')
 i = r.recvline()
```
`merge` is [an external file](https://github.com/jlsajfj/Offset-2020/blob/main/optimizer/merge.py) used to clean up main code. The merge code is from [a geeks for geeks](https://www.geeksforgeeks.org/counting-inversions/) post.
## Final Code
```python
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
```