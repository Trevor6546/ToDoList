from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

#allows user to add "to-do" to their list
@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.form['todo']
    todos.append({'task': todo, 'completed': False})  
    return redirect(url_for('index'))

#checks off listing
@app.route('/complete/<int:index>')
def complete_todo(index):
    if 0 <= index < len(todos):
        todos[index]['completed'] = True  
    return redirect(url_for('index'))

#allows user to delete from their todo list
@app.route('/delete/<int:index>')
def delete_todo(index):
    if 0 <= index < len(todos):
        del todos[index]  
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
