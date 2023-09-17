list_one =[]
list_prime =[]

print('Enter 5 numbers for lsit 1:')
for i in range(5):
    n= int(input())
    list_one.append(n)


for i in list_one:
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        list_prime.append(i)


print(list_prime)

for  i in list_prime:
    print(i)
