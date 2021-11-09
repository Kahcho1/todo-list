from application import app, db
from application.models import Tasks
from application.forms import TaskForm
from flask import render_template, request, redirect, url_for

@app.route('/')
@app.route('/home')
def home():
    all_task = Tasks.query.all()
    return render_template('index.html', title="Home Page", all_tasks=all_task)

@app.route('/create/task', methods=['GET', 'POST'])
def create_task():
    form = TaskForm()

    if request.method == 'POST':
        task_new = Tasks(desc=form.desc.data)
        db.session.add(task_new)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("create_task_form.html", title="Adding a new task", form=form)

@app.route('/read/allTasks')
def read_task():
    all_task = Tasks.query.order_by(Tasks.desc.asc()).all()
    t_dict = {"tasks": []}

    for task in all_task:
        t_dict["tasks"].append(
            {
                str(task.id) + " " + "Description of task": task.desc,
                "Completed": task.comp
            }
        )
    return t_dict

@app.route('/update/task/<int:id>', methods=['GET', 'POST'])
def update_task(id):
    form = TaskForm()
    task = Tasks.query.get(id)

    if request.method == 'POST':
        task.desc = desc=form.desc.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('update_task_form.html', task=task, form=form)

@app.route('/delete/task/<int:id>') # delete
def delete(id):
    task = Tasks.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/complete/task/<int:id>')
def status(id):
    task = Tasks.query.get(id)
    task.comp = True
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/incomplete/task/<int:id>')
def status_incomp(id):
    task = Tasks.query.get(id)
    task.comp = False
    db.session.commit()
    return redirect(url_for('home'))