import psycopg2
import sys

con = None
 
try:
	con = psycopg2.connect("host='localhost' dbname='supportGroupConnect' user='postgres' password='password'")   
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS Users, Friends, Condition, Messages")

	cur.execute("CREATE TABLE Users(id SERIAL, Username VARCHAR(20), Password VARCHAR(20))")
	cur.execute("INSERT INTO Users (username, password) VALUES('ImMarsh','password123')")
	cur.execute("INSERT INTO Users (username, password) VALUES('EZMoney','321password')")
	cur.execute("INSERT INTO Users (username, password) VALUES('Doorick','456password')")
	cur.execute("INSERT INTO Users (username, password) VALUES('Gloasi','password456')")
	cur.execute("INSERT INTO Users (username, password) VALUES('Salcidoo','passwordpassword')")

	cur.execute("CREATE TABLE Friends(friendship_ID SERIAL PRIMARY KEY, id INTEGER, friend_name VARCHAR(20))")
	cur.execute("INSERT INTO Friends (id, friend_name) VALUES('1','EZMoney')")
	cur.execute("INSERT INTO Friends (id, friend_name) VALUES('2','Doorick')")
	cur.execute("INSERT INTO Friends (id, friend_name) VALUES('3','Gloasi')")
	cur.execute("INSERT INTO Friends (id, friend_name) VALUES('4','ImMarsh')")
	cur.execute("INSERT INTO Friends (id, friend_name) VALUES('5','Doorick')")


	cur.execute("CREATE TABLE Condition(id INTEGER PRIMARY KEY, condition VARCHAR(20))")
	cur.execute("INSERT INTO Condition VALUES(1,'depression')")
	cur.execute("INSERT INTO Condition VALUES(2,'pneumonia')")
	cur.execute("INSERT INTO Condition VALUES(3,'PTSD')")
	cur.execute("INSERT INTO Condition VALUES(4,'broken_arm')")
	cur.execute("INSERT INTO Condition VALUES(5,'broken_ankle')")  
	
	cur.execute("CREATE TABLE Messages(message_id SERIAL, sender_id INTEGER, receiver_id INTEGER, message VARCHAR(255))")
	cur.execute("INSERT INTO Messages(sender_id, receiver_id, message) VALUES(1, 2, 'how is it hanging, bro?')")
	cur.execute("INSERT INTO Messages(sender_id, receiver_id, message) VALUES(2, 1, 'it is hanging lit, bro')")

	
	con.commit()
    
except psycopg2.DatabaseError as e:
	if con:
		con.rollback()
	print("printing error...")
	print ('Error %s' % e )   
	sys.exit(1)
 
finally:   
    if con:
        con.close()
