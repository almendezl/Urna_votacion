#!/usr/bin/python
import sqlite3
conn = sqlite3.connect('urna.db')
print ("Opened database successfully");

conn.execute("UPDATE VOTOS set CAND2=CAND2+1 where ID=1")


conn.commit()
print ("Records created successfully");
conn.close()
