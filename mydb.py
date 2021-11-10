import sqlite3


conn = sqlite3.connect('cert_db_old.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS cert_db(
   cert_id INTEGER PRIMARY KEY,
   thickness TEXT,
   metal_grade TEXT,
   gost TEXT,
   melting_number TEXT,
   batch_number TEXT,
   certificate_number TEXT,
   date_of_certificate TEXT,
   limit_fluidity TEXT,
   temporary_resistance TEXT,
   relative_extension TEXT,
   relative_narrowing TEXT,
   impact_strength_before_aging TEXT,
   impact_strength_after_aging TEXT,
   sample_type TEXT,
   impact_strength_below_zero TEXT,
   temperature_below_zero TEXT,
   sample_type_below_zero TEXT,
   additional_data TEXT);
""")

conn.commit()

cert = [
  ('1458-18785', 'лист 8х1500х6000'),
  ('14545-456456', 'лист 12х1500х6000'),
  ('4568-1546', 'лист 16х1500х6000'),
  ('888-456456', 'лист 12х1500х6000')
]

#cur.execute("""INSERT INTO cert_db VALUES('0001', '1458-18785', 'лист 12х1500х6000');""")
#cur.execute("""INSERT INTO cert_db VALUES('0002', '888-18785', 'лист 16х1500х6000');""")
#cur.execute("""INSERT INTO cert_db VALUES('0003', '888-18785', 'лист 16х1500х6000');""")

cur.execute("SELECT * FROM cert_db;")
three_results = cur.fetchall()
print(three_results)