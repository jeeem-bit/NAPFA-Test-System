from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', ['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template("form.html")
    else:
        gender, assyear, birthyear, results = request.form["gender", "assyear", "birthyear", "results"]
        
