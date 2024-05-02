import sqlite3 as sql
from flask import Flask, render_template, url_for, request, redirect                                        # From module flask import class Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

#database configuration
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

@app.route('/home_page')
def index():
    return render_template('homecategories.html')


@app.route('/browse_found')
def pull_found():
    con = sql.connect(r"C:\Users\yjain24\Documents\lost_found.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select post_id,title,time_posted,image,category from lost_found where category='found'")
    rows = cur.fetchall();

    for post_id,title,time_posted,image,category in rows:
        render_template('foundlist.html', )