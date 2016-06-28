from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsASecret'

# Set session like so:
# Remove something from session like so:
# session.pop('someKey')

@app.route('/')
def index():

	if "random" in session:
		pass
	else:
		session['random'] = random.randrange(0, 101)
	if "guess" in session:
		return render_template('index.html', random=session['random'], guess=session['guess'])
	else:
		return render_template('index.html', random=session['random'])


@app.route('/submit', methods=["post"])
def user_guess():		

	
	# if session['guess'] == None: 
	# 	return redirect('/')
	session['guess'] = int(request.form['number']) 
	return redirect('/')

@app.route('/reset')	
def clear():
	session.clear()
	return redirect('/')

app.run(debug=True)



# to redirect: return redirect('/route_goes_here')