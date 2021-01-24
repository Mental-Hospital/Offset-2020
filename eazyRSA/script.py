import gmpy

c = 3708354049649318175189820619077599798890688075815858391284996256924308912935262733471980964003143534200740113874286537588889431819703343015872364443921848
e = 16
p = 75000325607193724293694446403116223058337764961074929316352803137087536131383
q = 69376057129404174647351914434400429820318738947745593069596264646867332546443
phi = 5203226874048586660123187369475542584442690830335849146139399959453354953924976900388993415470710574187687844214029203747760116730703556445063231528642844
n = 5203226874048586660123187369475542584442690830335849146139399959453354953925121276771730013369651620548525360866907860251668937253089505512847186397320669

def decrypt(p, q, e, c):
 n = p*q
 count = 0
 max_i = 0
 candidate_found = False
 candidate = gmpy.mpz(c)
 while not candidate_found:
  candidate_found = True
  for i in range(0,4):
   if not gmpy.is_square(candidate):
    print("failed at ", i)
    if i > max_i:
     max_i = i
    print("max_i: ", max_i)
    print(candidate)
    candidate_found = False
    break
  if candidate_found:
   break
  count+=1
  print("Trying count = ", count)
  candidate += n
 
 candidate_root = candidate.root(16)[0]
 
 return candidate_root
print(decrypt(p, q, e, c))