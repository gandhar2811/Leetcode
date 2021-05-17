import collections
s = "Tree"
c = collections.Counter(list(s))
print(c)
a = sorted(c, key= lambda x: c[x],reverse= True)
print(a)
output = []
for char in a:
    output.append(char*c[char])
print("".join(output))