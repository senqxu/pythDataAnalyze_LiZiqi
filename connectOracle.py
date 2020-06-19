import cx_Oracle as oracle

db = oracle.connect('l3main/trust@10.80.117.30:1521/l3dev')
cursor = db.cursor
cursor.execute('select column_name,tale_name from user_tab_column_name like '*'')
data = cursor.fetchone
print(data)
cursor.close()
de.close()