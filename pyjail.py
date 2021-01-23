# not needed as of right now (2021 01 23)
payload = ""
out = ""
for _ in payload:
 out+="chr({})+".format(ord(_))
out = out[:-1]
print(out)