try:
    with open('kvr.data', 'x') as fp:
        print('--------------------------')
        print('File  creat newly and open in write mode succesfully')
        print('Name of the File:{}'.format(fp.name))
        print('File mode:{}'.format(fp.mode))
        print('Is file readable ?={}'.format(fp.readable()))
        print('Is file writadable ?={}'.format(fp.writable()))
        print('Is file closed=', fp.closed)
        print('--------------------------')
except FileExistsError:
    print('File already exist')
