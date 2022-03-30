from flask import Flask, render_template, request, redirect, url_for
from config import config
from controller import *
from person import *

app=Flask(__name__)

@app.route('/')
def index():
	return redirect(url_for('main'))

@app.route('/main', methods=['GET', 'POST'])
def main():
	if request.method == 'POST':
		#Get the variables from the form sent by POST method
		usr= request.form['username']
		psw= request.form['password']
		address= request.form['adrs']
		city= request.form['city']
		state= request.form['state']
		zipCode= request.form['zip']
		mPerson = person(usr,psw,address,city,state,zipCode)

		mController = controller(mPerson)
		print(mController.saveData())

		return render_template('auth/main.html')
	else:
		mController = controller("Hola mundo vista ")
		print(mController.saludar())	
		return render_template('auth/main.html')

if __name__=='__main__':
	app.config.from_object(config['development'])
	app.run()