#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('urna.db')
print ("Opened database successfully");

conn.execute("SELECT CAND1,CAND2,CAND3,CAND4,CAND5,BLANCO AS suma FROM VOTOS");



conn.commit()
print ("Records created successfully");
conn.close()
