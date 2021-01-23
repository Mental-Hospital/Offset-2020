payload = "import subprocess"
out = ""
for _ in payload:
 out+="chr({})+".format(ord(_))
out = out[:-1]
print(out)