my_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 5}

print(my_dict)
print(sorted(my_dict.values()))
print(sorted(my_dict.values(),reverse=True))


temp ={}

for k,v in my_dict.items():
    temp.update({v:k})
    print('{}:{}'.format(k,v))

