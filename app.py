from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = []


@app.route('/complete/<int:index>')
def complete_todo(index):
    if 0 <= index < len(todos):
        todos[index]['completed'] = True  
    return redirect(url_for('index'))


