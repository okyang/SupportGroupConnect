from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, escape
import os
import psycopg2
import sys

app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:	
        return "Hi"

@app.route('/login', methods=['POST'])
def do_admin_login():

	con = psycopg2.connect("host='localhost' dbname='supportGroupConnect' user='postgres' password='password'")   
	cur = con.cursor()
  cur.execute("SELECT username  FROM users WHERE users.username = '" + request.form['username']+ "'")
  
  username = cur.fetchone()
  
	cur.execute("SELECT password  FROM users WHERE users.username = '" + request.form['username']+ "'")
	
	password = cur.fetchone()
	
	con.commit()
  
  session['username'] = request.form['username'] #currently putting username into the session (not checking if it exists in the date base)
	
	if password is not None and request.form['password'] == password[0]:
		session['logged_in'] = True
	else:
		flash('That\'s the wrong password!')

	return home()
	
@app.route('/createaccount')
def loadcreateaccount():
	return render_template('createaccount.html', createaccountforreal = createaccountforreal)
	
@app.route('/createaccountforreal', methods = ['POST'])
def createaccountforreal():
	con = psycopg2.connect("host='localhost' dbname='supportGroupConnect' user='postgres' password='password'")   
	cur = con.cursor()
	cur.execute("INSERT INTO users (username, password) VALUES ('" + request.form['username'] + "', '" + request.form['password'] + "')")
	return render_template('login.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    session['logged_in'] = False
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)#host='0.0.0.0', port=4000)