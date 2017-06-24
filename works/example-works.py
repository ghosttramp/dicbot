#create db with date, open db, insirt value, save, close
import sqlite3
import datetime


conn = sqlite3.connect('dict.db')
c = conn.cursor()

c.execute('''CREATE TABLE words 
	         (date text, words text, translations text, mnemonics text)''')
c.execute("INSERT INTO words VALUES (datetime(),'a table', 'стол', 'фейсом об стол')")
conn.commit()
conn.close()

#insert with utf8
import sqlite3,datetime
var0 = input("Please enter a word: ")
var1 = input("Please enter translation: ")
var2 = input("Please enter mnemonic: ")
now = datetime.datetime.now()
conn = sqlite3.connect('dict.db')
c = conn.cursor()

#c.execute("INSERT INTO words VALUES (datetime(), var0, var1, var2)")
c.execute("INSERT INTO words (date,words,translations,mnemonics) VALUES(?,?,?,?)", (now,var0,var1,var2))

conn.commit()
conn.close()

#create table with id 

import sqlite3
import datetime

conn = sqlite3.connect('dict.db')
c = conn.cursor()
c.execute('''CREATE TABLE words 
	         (id INTEGER PRIMARY KEY AUTOINCREMENT, date text, words text, translations text, mnemonics text)''')
conn.commit()
conn.close()