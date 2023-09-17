def vowelOr(str):
    temp =str
    vowel=['a','e','i','o','u']

    for i in vowel:
        if(str == i):
            return True

        else:
            return False

str =input('Enter a character:')
if(vowelOr(str) == True):
    print('it is Vowel')
else:
    print('it is Consonant')
