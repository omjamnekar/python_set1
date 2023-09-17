class GradeError(Exception):
    def __init__(self):
       self.msg ='Invalid Error'
class FailError(Exception):
    def __init__(self):
        self.msg = 'Failed'


try:
    n = input('Enter a Grade:')
    if n.upper() not in ['O','A','A+','B+','B','C','D','F']:
      raise GradeError
    elif(n =='F'):
        raise FailError
except GradeError as error:
    print(error.msg)

except FailError as error:
    print(error.msg)

else:
    print('pass')
