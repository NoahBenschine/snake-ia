import psycopg2
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
setup_path = join(dirname(__file__), 'etc',"setup.sql")
print(setup_path)
load_dotenv(dotenv_path)
fd = open(setup_path, 'r')
sqlFile = fd.read()
db_pass = os.environ.get("DB_PASSWORD")


# all SQL commands (split on ';')

#with open(seti[_path], 'r') as sql_file:connection.executescript(sql_file.read())
try:
    connection = psycopg2.connect(database="d26bvkku1b2c1m", user = "lxfeqgaardprbv", password = db_pass, host = "ec2-52-54-38-229.compute-1.amazonaws.com", port = "5432")
    cursor = connection.cursor()

    sqlCommands = sqlFile.split(';')

    # Execute every command from the input file
    for command in sqlCommands[:-1]:
            cursor.execute(command)

except(Exception) as error:
    print("error while connecting to database",error)

finally:
    if(connection):
        cursor.close()
        connection.commit()
        connection.close()
