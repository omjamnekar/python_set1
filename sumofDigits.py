n= input('Enter a number:')

rev=0
rem=0
temp= int(n)
while(temp != 0):
    rem = temp%10
    rev= rev+(rem**3)
    temp//=10


print('The Sum of cube of digit is:',rev)
