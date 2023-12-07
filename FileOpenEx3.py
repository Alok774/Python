try:
    with open('stud1.data') as fp:
        print('File  Opened in read  mode succes')
        print('type of fp=', type(fp))
        print('Is file closed=', fp.closed)
        print('------------------------------')
except FileNotFoundError:
    print('File does not exist')
finally:
    print('I am from finally block')
    print('Is file closed=', fp.closed)


