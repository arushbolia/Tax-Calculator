from application import app, db
from flask import render_template, request, Response, json, redirect, flash, url_for, session


@app.route('/')
@app.route('/index')
def index():
    return "<h1>Hello Earth</h1>"
