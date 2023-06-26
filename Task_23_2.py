import pandas as pd
import matplotlib.pyplot as plt
from clickhouse_driver import connect


conn = connect(database="vh_vika", user="vika", password="VikaCH123", host="136.243.33.23", port='9000')
cur = conn.cursor()
cur.execute(f'''select * from vh_vika.book''')
conn.commit() #- сохранить изменения в бд
res1 = cur.fetchall()
cur.execute(f'''DESCRIBE TABLE vh_vika.book''')
res2 = cur.fetchall()
names = []
for i in res2:
    names.append(i[0])
conn.close()
df = pd.DataFrame(columns = names)
for i in res1:
    df.loc[len(df)]=list(i)
print(df)
df.plot('book_id','amount')
plt.show()
df.plot('book_id','price')
plt.show()
conn.close()

