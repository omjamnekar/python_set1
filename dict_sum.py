d = {'a':1,'b':4,'c':7,'g':2}

sum1=0
for k,v in d.items():
    sum1+=v

print('the sum of value:',sum1)    
print('sum={}'.format(sum(d.values())))
