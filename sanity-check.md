# Sanity Check

Dunno what I did but it worked. Connected to `https://www.rinkeby.io/` and dropped in the address `0x5CDd53b4dFe8AE92d73F40894C67c1a6da82032d`. Decompilation revealed
```
#
#  Panoramix v4 Oct 2019 
#  Decompiled source of rinkeby:0x5CDd53b4dFe8AE92d73F40894C67c1a6da82032d
# 
#  Let's make the world open source 
# 

const welcome = 'flag{1t_1s_jus7_th3_st@rt}'

#
#  Regular functions
#

def _fallback() payable: # default function
  revert
```
There's the flag! `flag{1t_1s_jus7_th3_st@rt}`
