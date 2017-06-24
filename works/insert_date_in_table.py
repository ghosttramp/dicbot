#for x in range(0, 4):
#    print ("We're on time %d" % (x))
#print 4 were on time

import sqlite3
import datetime


conn = sqlite3.connect('dict.db')
c = conn.cursor()

c.execute("INSERT INTO words VALUES (datetime(),'a song', 'песня, петь', 'сонг - бонг - петь')")
conn.commit()
conn.close()