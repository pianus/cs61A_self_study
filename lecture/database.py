import sqlite3

db = sqlite3.Connection("n.db")
db.execute("CREATE TABLE nums SELECT 2 UNION SELECT 3;")
db.execute("INSERT INTO nums VALUES (?), (?), (?)", range(4,7))
