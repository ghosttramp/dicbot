# -*- coding: utf-8 -*-

#var0 = input("Please enter word: ")
#var1 = input("Please enter word: ")
#print ("your entered a word: " + var0)
#print ("your entered translation: " + var1)

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