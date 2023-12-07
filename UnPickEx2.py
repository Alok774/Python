# wrp prg. which will reading the student records from the file
import pickle
with open('stud.data','rb') as fp:
    print('-' * 10)
    while(True):
        try:
            obj=pickle.load(fp)
            for val in obj:
                print('{}'.format(val),end='\t')
            print()
        except EOFError:
            print('-'*10)
            break



