#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import telebot
import config
import os
import time
import random
#import SQLighter
import sqlite3
#from telebot import types
#bot = telebot.TeleBot(config.token)
conn = sqlite3.connect('music.db')

cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")

# Получаем результат сделанного запроса
results = cursor.fetchall()
results2 =  cursor.fetchall()

print(results)  

c = conn.cursor()