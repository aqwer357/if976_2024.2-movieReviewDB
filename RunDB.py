import psycopg2
import os

conn = psycopg2.connect(dbname="localhost",
                        host="localhost",
                        user="postgres",
                        password="pass",
                        port= 5432)

cursor = conn.cursor()
cursor = conn.cursor()
script_dir = os.path.dirname(__file__)

dbFolderPath =  os.path.dirname(script_dir + '/esquema-fisico')

createDBFile = open(dbFolderPath + '/CRIACAO.sql')
insertFile = open(dbFolderPath + '/POVOAMENTO.sql')

print('is DB initialized? Type Y/N')

ans = input()

if ans == 'N':
    cursor.execute(createDBFile.read())
    cursor.execute(insertFile.read())

while ans != 'QUIT':
    ans = input()