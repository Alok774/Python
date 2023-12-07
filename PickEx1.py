#wrp prog. whiclh will acept multiple stud. info from key board and save those student in details.
import pickle
with open('stud.data','ab') as fp:
    while(True):
        lst=[]
        print('-'*50)
        sno=int(input('Enter student No.:'))
        sname=input('Enter student Name:')
        marks=float(input('Enter student Marks:'))
        lst.append(sno)
        lst.append(sname)
        lst.append(marks)
        pickle.dump(lst,fp)
        print('Student data save  succesfully')
        print('-' * 50)
        print(lst)
        ch=input('Do you want to save another record(yes/no):')
        if ch.lower()=='no':
            break
        


