def length1(list1):
    count =0
    for i in list1:
        count+=1
    return count
str = input('Enter a string:')

print('the langth of the String is:',length1(str))



list_num= [5,4,3,3,7,4]

print('the length of the list number is:',length1(list_num))

list_str= ['om','sarthak','patty','yash']

print('the length of the list string is:',length1(list_str))
