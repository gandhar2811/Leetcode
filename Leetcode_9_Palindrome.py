a = 129
b = 0
c = a
while a>0:
    b = (b*10)+(a%10)
    a//=10
if b==c:
    print(True)
else:
    print(False)
