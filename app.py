from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index(): 
    return render_template("index.html")
def image():  
    return app.send_static_file('index.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/payment')
def payment(): 
    return render_template("payment.html")