list_num =[]

list_odd=[]
list_even =[]

print('Enter 10 number:')
for i in range(10):
    n = int(input())
    list_num.append(n)


for num in list_num:
    if num%2==0:
        list_even.append(num)
    else:
        list_odd.append(num)


print('\n odd number in the list:')
print(list_odd)

print('\n even number in the list:')
print(list_even)

