"""Datetime notes for assignment 2"""

"---------------------"
"Datetime Module"
"TWO WAYS TO IMPORT: from datetime import date | import datetime"
import datetime

datetime.date(2022, 11, 3)
d1 = datetime.date(2022, 11, 3)
type(d1) # = <class 'datetime.date'>
d1.isoweekday() # = 4
d1.strftime("%d of %B (which is a %A") # = '03 of November (which is a Thursday)'

s = '11/9/1980' # == use s.split('/')"
[int(part) for part in s.split('/')]
# will give [11, 9, 1980]

# example
values = [int(part) for part in s.split('/')]
d3 = datetime.date(values[2], values[1], values[0])
# is equal to: d3 = datetime.date(1980, 9, 11)
d3.isoweekday() # = 4

s = '11/9/1980' # == use s.split('/')"
datetime.datetime.strptime(s, "%d/%m/%Y")
# = datetime.datetime(1980, 9, 11, 0, 0)

d4 = datetime.datetime.strptime(s, "%d/%m/%Y")
#before wad DATE object this is DATETIME object
 # d4.minute = 0

today = datetime.date.today()
start_date = datetime.date(2022, 9, 18)
time = today - start_date

"""How to turn 'time' into days, weeks years ect"""
from dateutil import relativedelta
"""BETTER WAY: to avoid relativedelta.relativedelta.ect """
from dateutil.relativedelta import relativedelta
relativedelta(today, start_date) # = (years=+3, months=+10, days=+14)


