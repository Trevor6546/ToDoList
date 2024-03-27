from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

#allows the user to add a "todo" to their todo list
@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.form['todo']
    todos.append({'task': todo, 'completed': False})  
    return redirect(url_for('index'))

