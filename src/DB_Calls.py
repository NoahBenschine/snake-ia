
def insertTag(cursor,tag):
    cursor.execute("INSERT INTO tags(name) VALUES (%s)",[tag])

def getTagID(cursor,tag):
    cursor.execute("SELECT id FROM tags WHERE name=%s",[tag])
    id = cursor.fetchone()
    return id

def insertScore(cursor,tagId,score):
    cursor.execute("INSERT INTO scores(value,tagID) VALUES(%s,%s)",[score,tagId])

def getScores(cursor):
    cursor.execute("SELECT * FROM SCORES ORDER BY value DESC")
    scores = cursor.fetchall()
    return scores

def getScoresByTag(cursor,tagID):
    cursor.execute("SELECT * FROM SCORES WHERE tagID=% ORDER BY value DESC",[tagID])
    scores = cursor.fetchall()
    return scores
