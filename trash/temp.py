import datetime 
  
# datetime(year, month, day, hour, minute, second) 
a = datetime.datetime(2017, 6, 21, 18, 25, 30) 
b = datetime.datetime(2017, 6, 21, 18, 24, 30) 
  
# returns a timedelta object 
c = a-b  
print('Difference: ', c) 
print('c.total_seconds() :: ', c.total_seconds())

minutes = c.total_seconds() / 60
print('Total difference in minutes: ', minutes) 
  
# returns the difference of the time of the day 
minutes = c.seconds / 60
print('Difference in minutes: ', minutes)

print(' ---------------- ')

dic = {}
dic['aaa'] = 1
dic['bbb'] = 2
dic['ccc'] = 3

if 'aaa' in dic:
    print('tem')
else:
    print('nao tem')