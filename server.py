from flask import Flask, render_template, redirect, request
from mysqlconnection import MySQLConnector

app = Flask(__name__)

mysql = MySQLConnector(app, 'friendsdb')
print mysql.query_db("SELECT * FROM friend")

@app.route("/")
def index(): 
	return render_template('index.html', friends = mysql.query_db('SELECT name, age, friend_since FROM friend'))

@app.route('/new', methods=['POST'])
def add():
	print request.form
	mysql.query_db('INSERT INTO friend(name, age, friend_since) VALUES ("{}", "{}", "{}");'.format(request.form['name'], request.form['age'], request.form['friend_since']))
	
	return redirect('/')
	
app.run(debug=True)