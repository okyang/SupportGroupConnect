import psycopg2
import sys

con = None
 
try:
    con = psycopg2.connect("host='localhost' dbname='supportGroupConnect' user='postgres' password='password'")   
    cur = con.cursor()
    cur.execute("CREATE TABLE Users(id SERIAL, Username VARCHAR(20), Password VARCHAR(20))")
    cur.execute("INSERT INTO Users (username, password) VALUES('ImMarsh','password123')")
    cur.execute("INSERT INTO Users (username, password) VALUES('EZMoney','321password')")
    cur.execute("INSERT INTO Users (username, password) VALUES('Doorick','456password')")
    cur.execute("INSERT INTO Users (username, password) VALUES('Gloasi','password456')")
    cur.execute("INSERT INTO Users (username, password) VALUES('Salcidoo','passwordpassword')")
    
    cur.execute("CREATE TABLE Friends(Id INTEGER, friend_name VARCHAR(20), friendship_ID INTEGER PRIMARY KEY)")
    cur.execute("INSERT INTO Friends VALUES(1,'EZMoney','1')")
    cur.execute("INSERT INTO Friends VALUES(2,'Doorick','2')")
    cur.execute("INSERT INTO Friends VALUES(3,'Gloasi','3')")
    cur.execute("INSERT INTO Friends VALUES(4,'ImMarsh','4')")
    cur.execute("INSERT INTO Friends VALUES(5,'Doorick','5')")
    
    
    cur.execute("CREATE TABLE Condition(Id INTEGER PRIMARY KEY, condition VARCHAR(20))")
    cur.execute("INSERT INTO Condition VALUES(1,'depression')")
    cur.execute("INSERT INTO Condition VALUES(2,'pneumonia')")
    cur.execute("INSERT INTO Condition VALUES(3,'PTSD')")
    cur.execute("INSERT INTO Condition VALUES(4,'broken_arm')")
    cur.execute("INSERT INTO Condition VALUES(5,'broken_ankle')")  
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
