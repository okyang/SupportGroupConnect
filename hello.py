from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import psycopg2
import sys

app = Flask(__name__)

@app.route('/')
def home():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:	
		con = psycopg2.connect("host='localhost' dbname='supportGroupConnect' user='postgres' password='password'")
		cur = con.cursor()
		cur.execute("SELECT condition  FROM condition WHERE condition.id = '" +session['user_id']+"'")
		q_condition = cur.fetchone()
		con.close()
		return render_template('portal.html', username = request.form['username'], condition = q_condition)

@app.route('/login', methods=['POST'])
def do_admin_login():

	con = psycopg2.connect("host='localhost' dbname='supportGroupConnect' user='postgres' password='password'")   
	cur = con.cursor()
	
	cur.execute("SELECT password  FROM users WHERE users.username = '" + request.form['username']+ "'")
	password = cur.fetchone()
	
	if password is not None and request.form['password'] == password[0]:
		cur.execute("SELECT id  FROM users WHERE users.username = '" + request.form['username']+ "'")
		user_id = cur.fetchone()
	
		#cur.execute("SELECT condition  FROM condition WHERE condition.id = '" str(ID) "'")
		cur.execute("SELECT condition FROM condition INNER JOIN users ON " + str(user_id[0]) +" = condition.id")
		condition = cur.fetchone()
	
		session['logged_in'] = True
		session['condition'] = condition[0]
		session['user_id'] = str(user_id[0])
	else:
		flash('Invalid username/password; please try again.')

	con.close()
	return home()

@app.route('/createaccount')
def loadcreateaccount():
	return render_template('createaccount.html', createaccountforreal = createaccountforreal)
	
@app.route('/createaccountforreal', methods = ['POST'])
def createaccountforreal():
	con = psycopg2.connect("host='localhost' dbname='supportGroupConnect' user='postgres' password='password'")   
	cur = con.cursor()
	cur.execute("INSERT INTO Users (username, password, bio) VALUES ('" + request.form['username'] + "', '" + request.form['password'] + "', '')")
	con.commit()
	cur.execute("SELECT ID FROM users WHERE users.username = '" + request.form['username']+ "'")
		
	ID = cur.fetchone()[0]
	
	cur.execute("INSERT INTO Condition (id,condition) VALUES (" + str(ID) + ",'" + request.form['condition'] + "')")
	con.commit()
	con.close()
	return render_template('login.html')

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return home()
 
@app.route('/login/chatroomcancer')
def chatroomcancer():
	print("user2:  ", request.form['username'])
	return render_template('chatroomcancer.html') #username = request.form['username'])

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)
