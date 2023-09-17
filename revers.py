def reverse(num):
    temp =num
    rev=0
    while(temp!=0):
        rem= temp%10
        rev = rev*10+rem
        temp//= 10
    print('The reverse of the number is:',rev)
num =int(input('Enter a number:'))

reverse(num)
