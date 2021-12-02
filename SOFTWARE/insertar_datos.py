#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('urna.db')
print ("Opened database successfully");

conn.execute("INSERT INTO USUARIOS (ID,CEDULA,PRIMER_NOMBRE,SEGUNDO_NOMBRE,PRIMER_APELLIDO,SEGUNDO_APELLIDO,VOT,EXPEDICION) \
      VALUES (100, 1014737422, 'MARIA', 'PAULA', 'MENDEZ', 'LOPEZ', '0', '12.34.5678' )");



conn.commit()
print ("Records created successfully");
conn.close()
