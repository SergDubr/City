
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = " "
flag = 0
@app.route("/")
def index():
	flash("What is the name of this city?")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	global flag
	if (str(request.form['name_input']) == 'Rome' or str(request.form['name_input']) == 'rome'):
		flag = 1
		flash("Yeeees it is the capital of Italy! Let 's immortalize yours name: ")
	else:
		flag = 0
		flash("No, it is not " + str(request.form['name_input']) + "... It is Rome! Just out of curiosity, what is your name?")
	return render_template("index1.html")

@app.route("/gret", methods=['POST', 'GET'])
def greeter1():
	if (flag == 1):
		flash("From student to graduate, it’s time to immortalize your name, " + str(request.form['name_input1']))
	else:
		flash("You will never see your name on a Honor Wall, " + str(request.form['name_input1']) + "!")
	return render_template("index2.html")