from datetime  import datetime

UserInput = '2015-9-1 9:01:30'

Datetime = datetime.strptime(UserInput, '%Y-%m-%d %H:%M:%S')
print Datetime.timestamp()