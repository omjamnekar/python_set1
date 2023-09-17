s={'PY':'s1','OP':'s2','CN':'s3'}

s2 ={'DS':'s1','AM/MP':'s2'}

temp={}
temp.update(s)
temp.update(s2)


print(sorted(temp))


for k,v in temp.items():
    print('{}:{}'.format(k,v))
