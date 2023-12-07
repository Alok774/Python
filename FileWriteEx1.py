# Write a python pro which will write different adress label to the file.
print('--------------------------')
with open('Addr1.data','a') as kv:
    kv.write('Travis \n')
    kv.write('fno:2-5,sea side\n')
    kv.write('Numpy s/w foundation\n')
    kv.write('Nether Land\n')
    print('Data written to the file')
    print('--------------------------')