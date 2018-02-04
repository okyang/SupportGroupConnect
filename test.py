import psycopg2
import sys

con = None
 
try:
	con = psycopg2.connect("host='localhost' dbname='supportGroupConnect' user='postgres' password='password'")   
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS Users, Friends, Condition, Messages, Groups, Memberships")

	cur.execute("CREATE TABLE Users(id SERIAL, Username VARCHAR(20), Password VARCHAR(20), Bio VARCHAR(300))")
	cur.execute("INSERT INTO Users (username, password, Bio) VALUES('ImMarsh','password123','double yikes')")
	cur.execute("INSERT INTO Users (username, password, Bio) VALUES('EZMoney','321password','i hate my  friend marshall')")
	cur.execute("INSERT INTO Users (username, password, Bio) VALUES('Doorick','456password','so tired')")
	cur.execute("INSERT INTO Users (username, password, Bio) VALUES('Gloasi','password456','too much kpop')")
	cur.execute("INSERT INTO Users (username, password, Bio) VALUES('Salcidoo','passwordpassword','yadada')")

	cur.execute("CREATE TABLE Friends(friendship_ID SERIAL PRIMARY KEY, first_id INTEGER, second_id INTEGER)")
	cur.execute("INSERT INTO Friends (first_id, second_id) VALUES(1,2)")
	cur.execute("INSERT INTO Friends (first_id, second_id) VALUES(2,1)")
	cur.execute("INSERT INTO Friends (first_id, second_id) VALUES(1,4)")
	cur.execute("INSERT INTO Friends (first_id, second_id) VALUES(4,1)")


	cur.execute("CREATE TABLE Condition(id INTEGER PRIMARY KEY, condition VARCHAR(20))")
	cur.execute("INSERT INTO Condition VALUES(1,'depression')")
	cur.execute("INSERT INTO Condition VALUES(2,'pneumonia')")
	cur.execute("INSERT INTO Condition VALUES(3,'PTSD')")
	cur.execute("INSERT INTO Condition VALUES(4,'broken_arm')")
	cur.execute("INSERT INTO Condition VALUES(5,'broken_ankle')")  
	
	cur.execute("CREATE TABLE Messages(message_id SERIAL, sender_id INTEGER, receiver_id INTEGER, message VARCHAR(255))")
	cur.execute("INSERT INTO Messages(sender_id, receiver_id, message) VALUES(1, 2, 'how is it hanging, bro?')")
	cur.execute("INSERT INTO Messages(sender_id, receiver_id, message) VALUES(2, 1, 'it is hanging lit, bro')")
	
	cur.execute("CREATE TABLE Groups(group_id SERIAL, name VARCHAR(30))")
	cur.execute("INSERT INTO Groups(name) VALUES('general')")
	cur.execute("INSERT INTO Groups(name) VALUES('depression')")
	cur.execute("INSERT INTO Groups(name) VALUES('pneumonia')")
	cur.execute("INSERT INTO Groups(name) VALUES('PTSD')")
	cur.execute("INSERT INTO Groups(name) VALUES('broken_arm')")
	cur.execute("INSERT INTO Groups(name) VALUES('broken_ankle')")
	
	cur.execute("CREATE TABLE Memberships(membership_id SERIAL, group_id Integer, id Integer)")
	cur.execute("INSERT INTO Memberships(group_id, id) VALUES(1, 1)")
	

	
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
