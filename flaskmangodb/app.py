from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://admin:9876543210@flaskmangodb.meh8jnx.mongodb.net/test'
mongo = PyMongo(app)

messages = mongo.db.messages

@app.route('/')
def index():
    saved_messages = messages.find()
    return render_template('index.html', messages=saved_messages)

@app.route('/add', methods=['POST'])
def add_message():
    new_message = request.form.get('new-message')
    messages.insert_one({'text' : new_message})
    return redirect(url_for('index'))
