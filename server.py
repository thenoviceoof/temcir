from bottle import route, run

@route('/')
def root():
    return 'This is root'

run(host='localhost', port=8080, debug=True)
