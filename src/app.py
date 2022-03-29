from flask import Flask, render_template, request, redirect, url_for
from config import config

app=Flask(__name__)

@app.route('/')
def index():
	return redirect(url_for('main'))

@app.route('/main', methods=['GET', 'POST'])
def main():
	if request.method == 'POST':
		print(request.form['username'])
		print(request.form['password'])
		return render_template('auth/main.html')
	else:	
		return render_template('auth/main.html')

if __name__=='__main__':
	app.config.from_object(config['development'])
	app.run()