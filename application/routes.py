from application import app, db
from application.models import Tasks

@app.route('/')
@app.route('/home')
def home():
    return 'Homepage in progress . . . . .'

@app.route('/create/<task>')
def create_task(task):
    task_new = Tasks(desc=task)
    db.session.add(task_new)
    db.session.commit()
    return f"The task of {task} has be added to your todo list as id {task_new.id}!"

@app.route('/read/allTasks')
def read_task():
    all_task = Tasks.query.order_by(Tasks.desc.asc()).all()
    t_dict = {"tasks": []}
    for task in all_task:
        t_dict["tasks"].append(
            {
                "Description of task": task.desc,
                "Completed": task.comp
            }
        )
    return t_dict

@app.route('/update/task/<int:id>/<new_desc>')
def update_task(id, new_desc):
    task = Tasks.query.get(id)
    task.desc = new_desc
    db.session.commit()
    return f"Task with id {task.id} has been updated with {new_desc}."

@app.route('/delete/task/<int:id>') # delete
def delete(id):
    task = Tasks.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return f"The task with id {id} has been removed from the todo list."