try:
    fp=open('stud.data','r')
    print('type of fp=', type(fp))
    print('Is file closed=',fp.closed)
except FileNotFoundError:
    print('File does not exist')
else:
    print('File  Opened in read  mode succes')
finally:
    fp.close()
    print('Is file closed=',fp.closed)

