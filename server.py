from bottle import route, run

@route('/add')
def add_task():
    return 'Add a task'

@route('/list')
def list_tasks():
    return 'List some tasks'

@route('/')
def get_task():
    return 'Get a task to do'

run(host='localhost', port=8080, debug=True)
