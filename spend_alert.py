from clickhouse_driver import connect
import requests

conn = connect(database="vh_vika", user="vika", password="VikaCH123", host="136.243.33.23", port='9000')

cursor = conn.cursor()
api_url = 'https://api.telegram.org/bot'
api_token = '5231963347:AAFMI4hkUgfhb6hXAr1BfjzCbkQvG163YsU'
# chat_id = '-1001844760565'
chat_id = '-791364185'


# функция для выполнения скрипта
sql = f'''select concat(toString(rowNumberInAllBlocks() + 1), ') ', 'No spend yesterday: '), * from 
(select concat('network = ', network), concat('network_id = ', toString(network_id)), concat('max_date = ', toString(max_date))  from
(select max(date) max_date, network_id, b.name network from vh_vika.adstats a 
left join dict.ad_network b on a.network_id=b.peerclick_id 
where network_id IN ('2','16','117','84','85','130','72', '1', '62', '63', '3', '46', '52', '95','121','144','9', '110', '124')
group by network_id, network) where max_date <> toDate(now()-interval 1 day))'''
cursor.execute(sql)
res = cursor.fetchall()
print(res)
lst = []

for i in res:
    lst = '\n'.join(map(str, i))
    req = requests.get(f'{api_url}{api_token}/sendMessage',
    params=dict(chat_id=f'{chat_id}', text=f'{lst}'))
    print(lst)


sql = f'''select concat(toString(rowNumberInAllBlocks() + 1), ') ', 'Spending appeared: '), * from 
(select concat('network = ', network), concat('network_id = ', toString(network_id)), concat('max_date = ', toString(max_date))  from
(select max(date) max_date, network_id, b.name network from vh_vika.adstats a 
left join dict.ad_network b on a.network_id=b.peerclick_id 
where network_id IN ('72', '100', '125', '85')
group by network_id, network) where max_date = toDate(now()-interval 1 day))'''
cursor.execute(sql)
res = cursor.fetchall()
print(res)
lst1 = []

for i in res:
    lst1 = '\n'.join(map(str, i))
    req = requests.get(f'{api_url}{api_token}/sendMessage',
    params=dict(chat_id=f'{chat_id}', text=f'{lst1}'))
    print(lst1)


