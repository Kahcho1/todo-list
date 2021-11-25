from application import app, db
from application.models import Tasks
from flask import request, redirect, url_for, Response, jsonify

@app.route('/create/task', methods=['POST'])
def create_task():
    package = request.json
    task_new = Tasks(desc=package["description"])
    db.session.add(task_new)
    db.session.commit()
    return Response(f"Task with description has been added: {task_new.desc}", mimetype='text/plain')

@app.route('/read/allTasks', methods=['GET'])
def read_tasks():
    all_tasks = Tasks.query.all()
    t_dict = {"tasks": []}

    for task in all_tasks:
        t_dict["tasks"].append(
            {
                "id": task.id,
                "description": task.desc,
                "completed": task.comp
            }
        )
    return jsonify(t_dict)

@app.route('/read/tasks/<int:id>', methods=['GET'])
def read_task(id):
    task = Tasks.query.get(id)
    t_dict = {
                "id": task.id,
                "description": task.desc,
                "completed": task.comp
            }
    return jsonify(t_dict)

@app.route('/update/task/<int:id>', methods=['PUT'])
def update_task(id):
    package = request.json
    task = Tasks.query.get(id)
    task.desc = package["description"]
    db.session.commit()
    return Response(f"Task #{id} has been updated with description: {task.desc}", mimetype='text/plain')

@app.route('/delete/task/<int:id>', methods=['DELETE'])
def delete(id):
    task = Tasks.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return Response(f"Task #{id} has been deleted!", mimetype='text/plain')

@app.route('/complete/task/<int:id>', methods=['PUT'])
def status(id):
    task = Tasks.query.get(id)
    task.comp = True
    db.session.commit()
    return Response(f"Task #{id} status has been changed to completed.", mimetype='text/plain')

@app.route('/incomplete/task/<int:id>', methods=['PUT'])
def status_incomp(id):
    task = Tasks.query.get(id)
    task.comp = False
    db.session.commit()
    return Response(f"Task #{id} status has been changed to incompleted.", mimetype='text/plain')