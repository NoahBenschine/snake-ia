import psycopg2
import os

# importing module
import sys

# appending a path
sys.path.append('src')

# importing required module
import DB_Calls

from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
# setup_path = join(dirname(__file__), 'etc',"setup.sql")
# print(setup_path)
load_dotenv(dotenv_path)
# fd = open(setup_path, 'r')
# sqlFile = fd.read()
db_pass = os.environ.get("DB_PASSWORD")
connection = psycopg2.connect(database="d26bvkku1b2c1m", user = "lxfeqgaardprbv", password = db_pass, host = "ec2-52-54-38-229.compute-1.amazonaws.com", port = "5432")
# all SQL commands (split on ';')
#comments below create the tables.
# sqlCommands = sqlFile.split(';')
#
# # Execute every command from the input file
# for command in sqlCommands[:-1]:
#         cursor.execute(command)
#with open(seti[_path], 'r') as sql_file:connection.executescript(sql_file.read())

def insertTag(tag):
    connection = psycopg2.connect(database="d26bvkku1b2c1m", user = "lxfeqgaardprbv", password = db_pass, host = "ec2-52-54-38-229.compute-1.amazonaws.com", port = "5432")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tags(name) VALUES (%s)",[tag])
    cursor.close()
    connection.commit()
    connection.close()

def getTagID(tag):
    connection = psycopg2.connect(database="d26bvkku1b2c1m", user = "lxfeqgaardprbv", password = db_pass, host = "ec2-52-54-38-229.compute-1.amazonaws.com", port = "5432")
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM tags WHERE name=%s",[tag])
    id = cursor.fetchone()
    return id
    cursor.close()
    connection.commit()
    connection.close()

def insertScore(tagId,score):
    connection = psycopg2.connect(database="d26bvkku1b2c1m", user = "lxfeqgaardprbv", password = db_pass, host = "ec2-52-54-38-229.compute-1.amazonaws.com", port = "5432")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO scores(value,tagID) VALUES(%s,%s)",[score,tagId])
    cursor.close()
    connection.commit()
    connection.close()

def getScores():
    connection = psycopg2.connect(database="d26bvkku1b2c1m", user = "lxfeqgaardprbv", password = db_pass, host = "ec2-52-54-38-229.compute-1.amazonaws.com", port = "5432")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM SCORES ORDER BY value DESC")
    scores = cursor.fetchall()
    return scores
    cursor.close()

def getScoresByTag(tagID):
    connection = psycopg2.connect(database="d26bvkku1b2c1m", user = "lxfeqgaardprbv", password = db_pass, host = "ec2-52-54-38-229.compute-1.amazonaws.com", port = "5432")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM SCORES WHERE tagID=% ORDER BY value DESC",[tagID])
    scores = cursor.fetchall()
    return scores
    cursor.close()
