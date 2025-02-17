{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, render_template, request, redirect, url_for\
import sqlite3\
import os\
\
app = Flask(__name__)\
\
# SQLite setup\
conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mydatabase.db'))\
c = conn.cursor()\
c.execute('''CREATE TABLE IF NOT EXISTS mydatabase \
             (username TEXT, password TEXT, firstname TEXT, lastname TEXT, email TEXT)''')\
conn.commit()\
conn.close()\
\
@app.route('/login', methods=['GET', 'POST'])\
def login():\
    if request.method == 'POST':\
        username = request.form['username']\
        password = request.form['password']\
\
        # Connect to the database\
        conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mydatabase.db'))\
        c = conn.cursor()\
        c.execute("SELECT * FROM mydatabase WHERE username=? AND password=?", (username, password))\
        user = c.fetchone()\
        conn.close()\
\
        if user:\
            # Redirect to profile if login is successful\
            return redirect(url_for('profile', username=username))\
        else:\
            # If credentials are invalid, show the error page\
            return render_template('login_error.html')\
    return render_template('login.html')\
\
@app.route('/')\
def index():\
    return render_template('register.html')\
\
@app.route('/register', methods=['POST'])\
def register():\
    username = request.form['username']\
    password = request.form['password']\
    firstname = request.form['firstname']\
    lastname = request.form['lastname']\
    email = request.form['email']\
\
    conn = sqlite3.connect('/home/ubuntu/flaskapp/mydatabase.db')\
    c = conn.cursor()\
    c.execute("INSERT INTO mydatabase (username, password, firstname, lastname, email) VALUES (?, ?, ?, ?, ?)",\
              (username, password, firstname, lastname, email))\
    conn.commit()\
    conn.close()\
\
    return redirect(url_for('profile', username=username))\
\
@app.route('/profile/<username>')\
def profile(username):\
    conn = sqlite3.connect('/home/ubuntu/flaskapp/mydatabase.db')\
    c = conn.cursor()\
    c.execute("SELECT * FROM mydatabase WHERE username=?", (username,))\
    user = c.fetchone()\
    conn.close()\
\
    return render_template('profile.html', user=user)\
\
if __name__ == '__main__':\
    app.run(debug=True)}