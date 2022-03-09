import psycopg2
def insertTag(cursor,tag):
cursor.execute("INSERT INTO tags(name) VALUES(%s)",(tag))

def insertScore(cursor,tagId,score):
    cursor.execute("INSERT INTO scores(score,tagID) VALUES(%s,%s)",(score,tagId))
