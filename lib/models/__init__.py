import sqlite3

CONN = sqlite3.connect('eventflow.db')
cursor = CONN.cursor()