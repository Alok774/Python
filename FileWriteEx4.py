# program for reading the data from keyboard and write to the file
with open('hyd.data','a') as fp:
    print('Enter the data from keyboard (press @ to stop):')
    while(True):
        kbdata=input()
        if(kbdata=='@'):
            break
        else:
            fp.write(kbdata+'\n')
    print('Data Written to the file')