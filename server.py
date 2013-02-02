from bottle import (get,
                    post,
                    request,
                    route,
                    run,
                    static_file)
from jinja2 import Environment, FileSystemLoader
from pymongo import MongoClient
import pyjade

import os

env = Environment(loader=FileSystemLoader('templates/'),
                  extensions=['pyjade.ext.jinja.PyJadeExtension'])

connection = MongoClient('localhost', 27017)
db = connection.temcir

################################################################################
# utils

def render_template(template_path, **context):
    '''
    Basic util fn to wrap up template loading/rendering, which looks
    suspiciously like flask's render_template
    '''
    template = env.get_template(template_path)
    return template.render(**context)

################################################################################
# views

PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))

@get('/static/<filename:path>')
def static(filename):
    return static_file(filename, root=os.path.join(PROJECT_PATH, 'static'))

@get('/add')
def add_task():
    return render_template('task.jade')

@post('/add')
def add_task_endpoint():
    '''
    Add a task
    '''
    task = request.forms.get('task')
    tags = request.forms.get('tags')
    tags = tags.split(',')
    # create_task(task, tags, time.now(), order=None)
    return ''

@get('/list')
def list_tasks():
    '''
    List tasks for ordering
    '''
    # TODO: template
    return 'List some tasks'

@post('/list')
def order_tasks():
    '''
    Save the ordering of the tasks
    '''
    return ''

@get('/')
def get_task():
    '''
    Offer a couple tasks, along with fun, or choose from the backlog
    '''
    # TODO: template
    return 'Get a task to do'

@post('/')
def choose_task():
    '''
    POST back which task, and how long you will commit to it
    '''
    return ''

if __name__=='__main__':
    run(host='localhost', port=8080, debug=True)
