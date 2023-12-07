# program for different type of value
a=10
b=12.24
c=True
with open('sample.info','w') as fp:
    fp.write(str(a)+'\n')
    fp.write(str(b)+'\n')
    fp.write(str(c)+'\n')
    print('Data written to the file')