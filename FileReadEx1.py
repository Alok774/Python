# prog. for reading data from file
try:
    filename=input('Enter any file name:')
    with open(filename) as fp:
        filedata=fp.read() # print str
        print('--------------')
        print(filedata)
        print(type(filedata))
        print('--------------')
except FileNotFoundError:
    print('File does not exist')