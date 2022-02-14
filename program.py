# program.py
sum = 1 + 2
print(sum)
print('Hola desde consola')
from datetime import date
from os import environ
date.today()
print(date.today())
print("Today is: " + str(date.today()))

from datetime import *
from dateutil.relativedelta import *
now = datetime.now()
now = now + relativedelta(months=1, weeks=1, hours=10)
print(now)
python3 -m venv env
