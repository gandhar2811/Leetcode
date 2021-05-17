import collections
s = "Leetcode"
c = collections.Counter(s)
for i in range(len(s)):
    if c.get(s[i])==1:
        print(i)
print(-1)