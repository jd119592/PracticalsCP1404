"""OOP EXTRA"""

"use isinstance to check variable type"
# isinstance(x, bool) = False
"PEP8 Exampe usage: "
"Correct: isinstance(x, bool) = False"
"Incorrect: if type(obj) is type(1)"

"---------------------------"
"""What does x + y mean?
- two operands concatenating strings and mathematical addition
+ operator is overloaded"""

"Do This Now-------"
def __eq__(self, other):
    return self.age == other.age & self.name == other.name

def test(self, other):
    print(self == other)

"---------------------"
"Datetime Module"
import datetime
datetime.date(2022, 11, 3)
d1 = datetime.date(2022, 11, 3)
type(d1) # = <class 'datetime.date'>
d1.isoweekday() # = 4
d1.strftime("%d of %B (which is a %A") # = '03 of November (which is a Thursday)'


