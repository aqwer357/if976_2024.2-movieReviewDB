import psycopg2
import os

# edite aqui para executar corretamente
conn = psycopg2.connect(dbname="postgres",
                        host="localhost",
                        user="postgres",
                        password="pass",
                        port= 5432)

cursor = conn.cursor()

script_dir = os.path.dirname(__file__)

dbFolderPath = os.path.relpath('.\\esquema-fisico', script_dir)

createDBFile = open(dbFolderPath + '\\CRIACAO.sql')
insertFile = open(dbFolderPath + '\\POVOAMENTO.sql')

print('is DB initialized? Type Y/N')

ans = input()

if ans == 'N':
    cursor.execute(createDBFile.read())
    cursor.execute(insertFile.read())
    conn.commit()
    print('DB Initialized according to file parameters')

print('Awaiting input')

while ans != 'QUIT':
    ans = input()
    match ans:
        case 'drop':
            cursor.execute('DROP SCHEMA PUBLIC CASCADE;')
            cursor.execute('CREATE SCHEMA PUBLIC;')
            conn.commit()
        case 'repopulate':
            cursor.execute(createDBFile.read())
            cursor.execute(insertFile.read())
            conn.commit()
        case 'simpleSelect':
            print("Please input table then select targets")
            table = input()
            targets = input()
            cursor.execute('SELECT ' + targets + ' FROM ' + table + ';')
            result = cursor.fetchall()
            print(result)
        case 'inputRaw':
            print('Please input the entire SQL command you wish to execute')
            command = input()
            cursor.execute(command)
            if 'SELECT' in command:
                result = cursor.fetchall()
                print(result)

conn.commit()
conn.close()