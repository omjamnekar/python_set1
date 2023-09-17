sum = 0
list_num =[]
list_odd =[]

print('Enter a 10 number:')
for i in range(10):
    n = int(input())
    list_num.append(n)

for num in list_num:
    if num%2!=0:
        sum +=num
        list_odd.append(num)

print(list_odd)
print('the sum of Odd number in list is:',sum);
