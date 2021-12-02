#!/usr/bin/python

import sqlite3
conn = sqlite3.connect('urna.db')
print ("Opened database successfully");

conn.execute("UPDATE VOTOS set CAND1=0 where ID=1")
conn.execute("UPDATE VOTOS set CAND2=0 where ID=1")
conn.execute("UPDATE VOTOS set CAND3=0 where ID=1")
conn.execute("UPDATE VOTOS set CAND4=0 where ID=1")
conn.execute("UPDATE VOTOS set CAND5=0 where ID=1")
conn.execute("UPDATE VOTOS set BLANCO=0 where ID=1")
conn.commit()
print ("Records created successfully");
conn.close()
