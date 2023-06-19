from clickhouse_driver import connect
import requests

conn = connect(database="vh_vika", user="vika", password="VikaCH123", host="136.243.33.23", port='9000')

cursor = conn.cursor()
api_url = 'https://api.telegram.org/bot'
api_token = '5231963347:AAFMI4hkUgfhb6hXAr1BfjzCbkQvG163YsU'
# chat_id = '-1001844760565'
chat_id = '-791364185'

sql = f'''select concat(toString(rowNumberInAllBlocks() + 1), ') ', 'Loading is slow: '), * from
(select concat('max_full_date = ', toString(max_full_date)), concat('App = ', AppCode) from
(select (max(toDate(ReceiveTimestamp)) - interval 1 day) max_full_date, AppID, b.AppCode AppCode from apps.installs a
    left join dict.apps b on a.AppID=toUInt64(b.AppID)
    where AppID IN  ('3787795', '2814483', '4027036', '4119277', '4396357', '4388917', '2705206')
     group by AppID, AppCode)
 where max_full_date <> toDate(now()-interval 1 day))'''
cursor.execute(sql)
res = cursor.fetchall()
print(res)
lst = []

for i in res:
    lst = '\n'.join(map(str, i))
    req = requests.get(f'{api_url}{api_token}/sendMessage',
    params=dict(chat_id=f'{chat_id}', text=f'{lst}'))
    print(lst)
