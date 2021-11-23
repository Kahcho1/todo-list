from application import app
from application.forms import TaskForm
from flask import render_template, request, redirect, url_for, jsonify
import requests

@app.route('/')
@app.route('/home')
def home():
    all_tasks = requests.get(f"http://todo-list-backend:5000/read/allTasks").json()
    app.logger.info(f"Tasks: {all_tasks}")
    return render_template('index.html', title="Home Page", all_tasks=all_tasks["tasks"])

@app.route('/create/task', methods=['GET', 'POST'])
def create_task():
    form = TaskForm()

    if request.method == 'POST':
        response = requests.post(
            f"http://todo-list-backend:5000/create/task",
            json={"description": form.desc.data})
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for('home'))

    return render_template("create_task_form.html", title="Adding a new task", form=form)

@app.route('/update/task/<int:id>', methods=['GET', 'POST'])
def update_task(id):
    form = TaskForm()
    task = requests.get(f"http://todo-list-backend:5000/read/tasks/{id}").json()
    app.logger.info(f"Tasks: {task}")

    if request.method == 'POST':
        response = requests.put(
            f"http://todo-list-backend:5000/update/task/{id}",
            json={"description": form.desc.data})
        return redirect(url_for('home'))

    return render_template('update_task_form.html', task=task, form=form)

# @app.route('/delete/task/<int:id>') # delete
# def delete(id):
#     task = Tasks.query.get(id)
#     db.session.delete(task)
#     db.session.commit()
#     return redirect(url_for('home'))

# @app.route('/complete/task/<int:id>')
# def status(id):
#     task = Tasks.query.get(id)
#     task.comp = True
#     db.session.commit()
#     return redirect(url_for('home'))

# @app.route('/incomplete/task/<int:id>')
# def status_incomp(id):
#     task = Tasks.query.get(id)
#     task.comp = False
#     db.session.commit()
#     return redirect(url_for('home'))