with open('kvr.data', 'a+') as fp:
    print('--------------------------')
    print('File read mode succesfully')
    print('Name of the File:{}'.format(fp.name))
    print('File mode:{}'.format(fp.mode))
    print('Is file readable ?={}'.format(fp.readable()))
    print('Is file writadable ?={}'.format(fp.writable()))
    print('Is file closed=', fp.closed)
    print('--------------------------')