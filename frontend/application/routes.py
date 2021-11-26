from application import app
from application.forms import TaskForm
from flask import render_template, request, redirect, url_for, jsonify
import requests

backend_host = "todo-list_backend:5000"

@app.route('/')
@app.route('/home')
def home():
    all_tasks = requests.get(f"http://{backend_host}/read/allTasks").json()
    app.logger.info(f"Tasks: {all_tasks}")
    return render_template('index.html', title="Home Page", all_tasks=all_tasks["tasks"])

@app.route('/create/task', methods=['GET', 'POST'])
def create_task():
    form = TaskForm()

    if request.method == "POST":
        response = requests.post(
            f"http://{backend_host}/create/task",
            json={"description": form.desc.data}
            )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for('home'))

    return render_template("create_task_form.html", title="Adding a new task", form=form)

@app.route('/update/task/<int:id>', methods=['GET', 'POST'])
def update_task(id):
    form = TaskForm()
    task = requests.get(
        f"http://{backend_host}/read/tasks/{id}").json()
    app.logger.info(f"Tasks: {task}")

    if request.method == "POST":
        response = requests.put(
            f"http://{backend_host}/update/task/{id}",
            json={"description": form.desc.data}
            )
        return redirect(url_for('home'))

    return render_template('update_task_form.html', task=task, form=form)

@app.route('/delete/task/<int:id>')
def delete(id):
    response = requests.delete(f"http://{backend_host}/delete/task/{id}")
    app.logger.info(f"Response: {response.text}")
    return redirect(url_for('home'))

@app.route('/complete/task/<int:id>')
def status(id):
    response = requests.put(f"http://{backend_host}/complete/task/{id}")
    app.logger.info(f"Response: {response.text}")
    return redirect(url_for('home'))

@app.route('/incomplete/task/<int:id>')
def status_incomp(id):
    response = requests.put(f"http://{backend_host}/incomplete/task/{id}")
    app.logger.info(f"Response: {response.text}")
    return redirect(url_for('home'))