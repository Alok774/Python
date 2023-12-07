#program for writting different type iterable object
x={10:'python',20:'Java',30:('kvr','hyd')}
with open('Iterobj.data','a') as fp:
    fp.writelines(str(x)+'\n')
    print('Data Written to the file')