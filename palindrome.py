def palindrome(num):
    temp =num
    rev= 0
    while(temp!=0):
        rem =temp%10
        rev =rev*10 +rem
        temp //= 10
    if(rev ==num):
        print('it is palindrome number')
    else:
        print('is is not palindrome number')

num = int(input('Enter a number:'))

palindrome(num)
