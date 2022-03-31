from flask import Flask, render_template, request, redirect, url_for
from config import config
from controller import *
from person import *

app=Flask(__name__)

@app.route('/')
def index():
	return redirect(url_for('main'))
#if another view is needed just create another def function and render its own template
@app.route('/main', methods=['GET', 'POST'])
def main():
	if request.method == 'POST':
		#Get the variables from the HTML form sent by POST method
		usr= request.form['username']
		psw= request.form['password']
		address= request.form['adrs']
		city= request.form['city']
		state= request.form['state']
		zipCode= request.form['zip']
		#create a Object person to be easier pass the parameter
		mPerson = person(usr,psw,address,city,state,zipCode)
		#initialize controller to chain the MVC
		mController = controller()
		#instead a log print, this could be more visible by a label in the HTML
		print(mController.saveData(mPerson))
		return render_template('auth/main.html')
	#GET
	else:
		#get the query param id
		mId=request.args.get("id")
		#if it has not query param id means that a html form must be shown
		if mId is None:
			return render_template('auth/main.html')
		else:
			#initialize controller to chain the MVC
			mController = controller()
			#make an API request to an specificly URL based into mId(query param)
			response=mController.requestUsr(mId)
			#mainResponse.html can be replace by just main.html but in this example are diferent to be easier of learn
			#in this case add response data (previously parced by controller) to be shown into the template
			return render_template('auth/mainResponse.html',data = response)
	
if __name__=='__main__':
	#config.py can be used to change the type of compilation and set te DB connection
	app.config.from_object(config['development'])
	app.run()