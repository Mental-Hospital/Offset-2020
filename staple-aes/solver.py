b1b3   = [0x0e,0x5d,0x12,0x38,0x0c,0x28,0x6a,0x68,0x28,0x6f,0x06,0x54,0x0b,0x06,0x6c,0x43]
flag_1 = []
flag_2 = []
flag_3 = [0x7d,0x0f,0x0f,0x0f,0x0f,0x0f,0x0f,0x0f,0x0f,0x0f,0x0f,0x0f,0x0f,0x0f,0x0f,0x0f]
for i in range(0, len(flag_1)):
	flag_2.append(b1b3[i]^flag_1[i])

for i in range(len(flag_1), len(b1b3)):
	flag1_possibilities = []
	flag2_possibilities = []
	for a in alpha_set:
		if (ord(a) ^ b1b3[i]).to_bytes(1, 'big') in alpha_set:
			flag1_possibilities.append(chr(ord(a)))
			flag2_possibilities.append(chr((ord(a) ^ b1b3[i])))
			continue
	print(flag1_possibilities, flag2_possibilities)
	print()
	print()

# >>> int('81bdc2ad2a484a1f84a3eda4add9fe45', 16)
# 172455704069538216526211312983758995013
# >>> b2 = int('81bdc2ad2a484a1f84a3eda4add9fe45', 16)
# >>> b3 = int('9adeacc55e0e1a27e39c97cccaa2ae7d', 16)
# >>> hex(b2 ^ b3)
# '0x1b636e6874465038673f7a68677b5038'
# >>> b3_p = 0x7d0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f
# >>> b2b3 = hex(b2 ^ b3)
# >>> b2b3 ^ b3p
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'b3p' is not defined
# >>> b2b3 ^ b3_p
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for ^: 'str' and 'int'
# >>> p b3_p
#   File "<stdin>", line 1
#     p b3_p
#       ^
# SyntaxError: invalid syntax
# >>> print(b3_p)
# 166231689355219479164323165303294856975
# >>> b2b3 = b2 ^ b3
# >>> b2b3 ^ b3_p
# 136143999223170831041079246489595961143
# >>> hex(b2b3 ^ b3_p
# ... )
# '0x666c61677b495f376830756768745f37'
# >>> b1b3 =  0x0e5d12380c286a68286f06540b066c43
# >>> b2_p = b2b3 ^ b3_p
# >>> hex(b1b3 ^ b2_p)
# '0x6831735f7761355f405f733363723374'
# >>> 
