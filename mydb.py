import sqlite3


conn = sqlite3.connect('cert_db.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS cert_db(
   cert_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   certificate_number TEXT,
   thickness TEXT);
""")
conn.commit()

cert = [
  ('1458-18785', 'лист 8х1500х6000'),
  ('14545-456456', 'лист 12х1500х6000'),
  ('4568-1546', 'лист 16х1500х6000'),
  ('888-456456', 'лист 12х1500х6000')
]

cur.execute("""INSERT INTO cert_db VALUES('0001', '1458-18785', 'лист 12х1500х6000');""")
cur.execute("""INSERT INTO cert_db VALUES('0002', '888-18785', 'лист 16х1500х6000');""")
cur.execute("""INSERT INTO cert_db VALUES('0003', '888-18785', 'лист 16х1500х6000');""")

cur.execute("SELECT rowid, cert_id FROM cert_db GROUP BY cert_id;")
three_results = cur.fetchall()
print(three_results)