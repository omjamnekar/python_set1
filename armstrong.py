def armstrong(num):
    temp = num
    rev= 0
    while(temp!=0):
        rem= temp%10
        rev= rev*10 + rem
        temp //=10
    if(rev==num):
         print('it is an Armstrong number')
    else:
        print('it is not an ArmStrong number')
        

num =int(input('Enter a number for Armstrong:'))

armstrong(num)
