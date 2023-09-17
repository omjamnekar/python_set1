num= int(input('Enter a number:'))

def fact(n):
    if(n ==1):
        return 1
    else:
        return fact(n-1)*n

print('the factorial of the number is:',fact(num))
