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

#allows the user to delete a "todo" from their todo list
@app.route('/delete/<int:index>')
def delete_todo(index):
    if 0 <= index < len(todos):
        del todos[index]  
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
