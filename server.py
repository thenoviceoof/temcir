from bottle import (get,
                    post,
                    redirect,
                    request,
                    route,
                    run,
                    static_file)
from jinja2 import Environment, FileSystemLoader
from pymongo import MongoClient
import pyjade

import random
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
# static files

PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))

@get('/static/<filename:path>')
def static(filename):
    return static_file(filename, root=os.path.join(PROJECT_PATH, 'static'))

################################################################################
# views

####################
# task addition
TASK_ADD_MAPPING = {
    'name': 'task-name',
    'notes': 'task-notes',
    'time': 'task-time',
    'snaptime': 'task-snaptime',
    'deadline': 'task-deadline',
    'tags': 'task-tags',
    }

@get('/add')
def add_task():
    return render_template('task.jade')

@post('/add')
def add_task_endpoint():
    data = {}
    for n,v in TASK_ADD_MAPPING.iteritems():
        tmp = request.forms.get(v)
        if tmp:
            data[n] = tmp
    # custom data handling
    if data.get('time'):
        data['time'] = float(data['time'])
    if data.get('tags'):
        data['tags'] = data['tags'].split(',')
    # do some basic data validation
    if set(['name', 'notes']) & set(data.keys()):
        # DEBUG
        print data
        db.tasks.insert(data)
    # don't do AJAX magic for MVP
    return redirect('/add')


####################
# task listing/priority sorting
@get('/list')
@get('/list/<num:int>')
def list_tasks(num=10):
    # get unsorted tasks
    unsorted_tasks = db.tasks.find({'order': {'$exists': False}})
    # get <num> sorted tasks
    sorted_tasks = db.tasks.find({'order': {'$exists': True}},
                                 sort=[('order', 1)])
    unsorted_tasks = list(unsorted_tasks)
    sorted_tasks = list(sorted_tasks[:num])
    return render_template('list.jade',
                           sorted_tasks = sorted_tasks,
                           unsorted_tasks = unsorted_tasks)

@post('/task/<id>')
def edit_task(id):
    return ''

@post('/list')
def order_tasks():
    # order tasks w/ midpoint between floats
    return ''


####################
# Task out

def weighted_choice(coll):
    '''
    Takes an ordered collection of [...(obj, weight)...], and returns
    an obj randomly, weighted by the weights
    '''
    total = sum(w for obj,w in coll)
    rw = random.random(0,total)
    cw = 0
    for i, ow in enumerate(coll):
        obj, w = ow
        cw += w
        if rw < cw:
            return obj, i
    raise ValueError

def get_top_tasks(num=3):
    tasks = db.tasks.find({'order': {'$exists': True}}, sort=[('order', 1)])
    weighted_tasks = [(t,0.9**i) for i,t in enumerate(tasks)]
    # choose randomly for now (weighted)
    chosen = []
    while len(chosen) < num and weighted_tasks:
        t, i = weighted_choice(weighted_tasks)
        chosen.append(t)
        weighted_tasks.pop(i)
    # don't have enough to fill it up? try getting some unweighted tasks
    if len(chosen) < num:
        tasks = list(db.tasks.find({'order': {'$exists': False}}))
        while len(chosen) < num and tasks:
            t = random.choice(tasks)
            chosen.append(t)
            i = tasks.index(t)
            del tasks[i]
    return chosen

@get('/')
def give_task():
    '''
    Offer a couple tasks, along with fun, or choose from the backlog
    '''
    tasks = get_top_tasks()
    # TODO: template
    return 'Get a task to do'

@post('/')
def choose_task():
    '''
    POST back which task, and how long you will commit to it
    '''
    return ''


####################
# main loop
if __name__=='__main__':
    run(host='localhost', port=8080, debug=True)
