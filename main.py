from flask import Flask, request, jsonify
from flask import render_template
from markupsafe import escape
from flask import redirect
from routes.home import home_route ##importando a blueprint para o dunfi.py
from routes.cliente import client_route

app = Flask('__Dunfi__')

app.register_blueprint(home_route)
app.register_blueprint(client_route, url_prefix = '/clientes')
#blueprint agrupa as rotas


if __name__ == "__main__":
    app.run(debug=True)


##app = Flask(__name__)
##
##tasks = []
##
##@app.route('/tasks', methods=['POST'])
##def add_task():
##    task = request.json
##    tasks.append(task)
##    return jsonify(task), 201
##
##@app.route('/tasks', methods=['GET'])
##def get_tasks():
##    return jsonify(tasks)
##
##@app.route('/tasks/<int:task_id>', methods=['GET'])
##def get_task(task_id):
##    if task_id < len(tasks):
##        return jsonify(tasks[task_id])
##    else:
##        return jsonify({'error': 'Task not found'}), 404
##
##@app.route('/tasks/<int:task_id>', methods=['DELETE'])
##def delete_task(task_id):
##    if task_id < len(tasks):
##        deleted_task = tasks.pop(task_id)
##        return jsonify(deleted_task)
##    else:
##        return jsonify({'error': 'Task not found'}), 404
##
##if __name__ == '__main__':
##    app.run(debug=True)