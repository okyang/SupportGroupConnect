from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, escape
import os
 
app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        if 'username' in session:
            user = session['username']
        return ('hello there', user)

@app.route('/login', methods=['POST'])
def do_admin_login():
    #request.form['username'] gets the user-input for username
    #need to get acceptable usernames w/ corresponding passwords 
    session['username'] = request.form['username']  
    if request.form['password'] == 'password':
        session['logged_in'] = True
    else:
        flash('That\'s the wrong password!')
    
    return home()


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    session['logged_in'] = False
    return redirect(url_for('home'))

"""
@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

"""
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)#,host='0.0.0.0', port=4000)