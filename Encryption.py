alphabets="abcdefghikjlmnopqrstuvwxyz"

pat="hello world".lower()
newpat=""

for i in range(len(pat)):
    if(pat[i] in alphabets):
        newpat+=alphabets[(alphabets.index(pat[i])+i)%26]
    else:
        newpat+=pat[i]
print(newpat)







