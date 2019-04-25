from bottle import request, route, run, static_file

@route('/')
def index():
    return static_file('index.html', './')

@route('/command')
def command():
    value = request.query.value
    print(value)
    return 'Value was set to: ' + value

run(host='0.0.0.0', port=8000, debug=True)
