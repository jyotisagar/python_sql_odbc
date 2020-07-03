import pyodbc

conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-ESENG68;'
    'Database=cspire;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()
cursor.execute('select * from provider')

for row in cursor:
    print(row)

conn.close()

