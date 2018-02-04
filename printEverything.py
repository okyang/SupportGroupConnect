import psycopg2
import sys

con = None
 
try:
	con = psycopg2.connect("host='localhost' dbname='supportGroupConnect' user='postgres' password='password'")   
	cur = con.cursor()
	cur.execute("SELECT * FROM users")
	row = cur.fetchone()
	print("User Table")
	while row != None:
		print(row)
		row = cur.fetchone()
	cur.execute("SELECT * FROM friends")
	row = cur.fetchone()
	print("\n Friend Table")
	while row != None:
		print(row)
		row = cur.fetchone()
	cur.execute("SELECT * FROM condition")
	row = cur.fetchone()
	print("\n Condition Table")
	while row != None:
		print(row)
		row = cur.fetchone()
	cur.execute("SELECT * FROM messages")
	row = cur.fetchone()
	print("\n Message Table")
	while row != None:
		print(row)
		row = cur.fetchone()
	cur.execute("SELECT * FROM groups")
	row = cur.fetchone()
	print("\n Groups Table")
	while row != None:
		print(row)
		row = cur.fetchone()
	cur.execute("SELECT * FROM memberships")
	row = cur.fetchone()
	print("\n Memberships Table")
	while row != None:
		print(row)
		row = cur.fetchone()

	
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
