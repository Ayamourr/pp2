#ex1
import datetime

today = datetime.date.today()
new_date = today - datetime.timedelta(days=5)
print("New date:", new_date)

#ex2
from datetime import datetime, timedelta

today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#ex3
from datetime import datetime

now = datetime.now()
new_now = now.replace(microsecond=0)

print(new_now)

#ex4
from datetime import datetime

d1 = datetime(2024, 2, 24, 15, 0, 0)
d2 = datetime(2024, 2, 25, 15, 0, 0)

diff = (d2 - d1).total_seconds()

print(diff)
