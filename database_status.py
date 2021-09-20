# Database Status

import MySQLdb as mysql
from rich.console import Console


console = Console()

# use sudo

db = mysql.connect(host = "localhost",user="root",passwd="123",db="INFORMATION_SCHEMA") #Database connection
cur = db.cursor()


cur.execute('SHOW STATUS') # Execute query
res = cur.fetchall() # Fetch all data
data = dict(res)

print("...................FIELDS.............................")
console.print(f"Threads_connected : {data['Threads_connected']}", style='bold green')
console.print(f"Threads_created : {data['Threads_created']}", style = 'bold green')
console.print(f"Threads_running : {data['Threads_running']}", style = 'bold green')
console.print(f"Uptime : {data['Uptime']}", style = 'bold green')
console.print(f"Queries : {data['Queries']}", style = 'bold green')
console.print(f"Max_used_connections : {data['Max_used_connections']}", style = 'bold green')

print("......................PROCESS LIST TABLE.................")
cur.execute("select * from PROCESSLIST") # Execute query
res2 = cur.fetchall()
for i in res2:
	console.print(f"ID | {i[0]} | USER INFO | {i[1]} | HOST | {i[2]} | DB | {i[3]} | COMMAND | {i[4]} | TIME | {i[5]} | STATE | {i[6]} | INFO | {i[7]}")
db.close()
