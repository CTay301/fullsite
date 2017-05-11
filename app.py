from flask import Flask, render_template, request, flash, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy





app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/TatuDaGawd/mysite/tmp/database.db'
db = SQLAlchemy(app)
app.secret_key = 'Tatu2k17'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resume')
def contact():
    return render_template('resume.html')

@app.route('/transcript')
def transcript():
    return render_template('transcript.html')
