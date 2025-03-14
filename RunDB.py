import psycopg2

conn = psycopg2.connect(dbname="localhost",
                        host="localhost",
                        user="postgres",
                        password="pass",
                        port= 5432)

cursor = conn.cursor()

var = input()
