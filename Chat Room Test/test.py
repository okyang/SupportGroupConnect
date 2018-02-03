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
    cur.execute("INSERT INTO Friends VALUES(11111,'EZMoney','1')")
    cur.execute("INSERT INTO Friends VALUES(22222,'Doorick','2')")
    cur.execute("INSERT INTO Friends VALUES(33333,'Gloasi','3')")
    cur.execute("INSERT INTO Friends VALUES(55555,'ImMarsh','4')")
    cur.execute("INSERT INTO Friends VALUES(44444,'Doorick','5')")
    
    
    cur.execute("CREATE TABLE Condition(Id INTEGER PRIMARY KEY, condition VARCHAR(20))")
    cur.execute("INSERT INTO Condition VALUES(11111,'depression')")
    cur.execute("INSERT INTO Condition VALUES(22222,'pneumonia')")
    cur.execute("INSERT INTO Condition VALUES(33333,'PTSD')")
    cur.execute("INSERT INTO Condition VALUES(55551,'broken_arm')")
    cur.execute("INSERT INTO Condition VALUES(55555,'broken_ankle')")  
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