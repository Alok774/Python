srcfile=input('Enter destination file:')
try:
    with open('srcfile','r') as fp1:
        desfile=input('Enter Destination file:')
        with open('desfile','a') as fp2:
            filedata=fp1.read()
            fp2.write(filedata)
            print('File copied--verify')

except FileNotFoundError:
    print("File doesn't exist")