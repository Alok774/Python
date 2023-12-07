try:
    with open('G:\Alok Pradhan\human.png','rb') as fp1:
        with open('hum1.png','wb') as fp2:
            imgdata=fp1.read()
            fp2.write(imgdata)
            print('image copied--verify')

except FileNotFoundError:
    print('File does not exist')