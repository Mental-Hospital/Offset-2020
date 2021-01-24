alphabet = "@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789"
alpha_set = [x.encode("utf-8") for x in list(alphabet)]
b1b3   = [0x0e,0x5d,0x12,0x38,0x0c,0x28,0x6a,0x68,0x28,0x6f,0x06,0x54,0x0b,0x06,0x6c,0x43]
flag_1 = [0x66,0x6C,0x61,0x67,0x7B]
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