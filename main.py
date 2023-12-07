lst=[1,232,5545455,999999,1212121,85358]
a=0
b=0
c=-1
for i in range(0,len(lst)):
    cv=str(lst[i])
    if cv==cv[::-1]:
        b=len(cv)
    if b>a:
        a=b
        c=i
else:
    print('Max palindrome Value={}'.format(lst[pos]))
    careers@centillionnetworks.com