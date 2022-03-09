
CREATE TABLE tags(
  id SERIAL PRIMARY KEY,
  name VARCHAR(30) NOT NULL
);

CREATE TABLE scores(
   scoreID SERIAL,
   value int NOT NULL,
   tagId int,
   PRIMARY KEY (scoreID),
   FOREIGN KEY (tagID) REFERENCES tags(id) ON DELETE CASCADE
);
