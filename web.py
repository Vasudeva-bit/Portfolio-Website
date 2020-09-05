from flask import Flask,render_template,request,redirect,url_for
import csv
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<string:urlname>')
def hello_world1(urlname):
    return render_template(urlname)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
	data=request.form.to_dict()
	fun1(data)
	return redirect('thanq.html')

def fun(data) :
	with open('database.txt','a') as file:
		email=data['email']
		subject=data['subject']
		message=data['message']
		file.write(f'\n{email},{subject},{message}')

def fun1(data) :
	with open('base.csv','a' ,newline='') as csvf:
		email=data['email']
		subject=data['subject']
		message=data['message']
		csvfile=csv.writer(csvf)
		csvfile.writerow(['email','subject','message'])
		csvfile.writerow([email,subject,message])





