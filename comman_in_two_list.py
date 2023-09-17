list_one =[]
list_two =[]

print('Enter 5 numbers for lsit 1:')
for i in range(5):
    n= int(input())
    list_one.append(n)

print('Enter 5 numbers for lsit 2:')
for i in range(5):
    n= int(input())
    list_two.append(n)


def comman(list_one,list_two):
    for i in list_one:
        for j in list_two:
            if( i== j):
                return True
            
if(comman(list_one,list_two) == True):
    print('there is a comman element')
else:
    print('there is no comman element')




