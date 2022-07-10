from bottle import route, run, template

@route('/')
def index():
	return f'<b>Hello GFG</b>!'

@route('/<name>')
def nom(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)


run(host='0.0.0.0', port=8000,debug=True)
