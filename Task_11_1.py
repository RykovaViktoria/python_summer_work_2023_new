import calendar
from datetime import date
for mo in range(1,13):
    month = calendar.monthrange(2023, mo)
    for i in range(1, month[1]+1):
        w = calendar.weekday(2023, mo, i)
        if w == 3:
            dt = date(2023, mo, i)
            print(dt.strftime('%d %B %Y'))
