# prog. for reading data from file
try:
    filename=input('Enter any file name:')
    with open(filename) as fp:
        filedata=fp.readlines()  # print List data
        print('--------------')
        print(filedata)
        print(type(filedata))
        print('--------------')
except FileNotFoundError:
    print('File does not exist')