from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/html')
def about():
	return render_template('index.html')
