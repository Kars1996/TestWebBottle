from bottle import run, route, template

@route('/')
def index():
    return '<h1>Helo, World!</h1>'

@route('/login')
def login():
    return "<h1>On the login page</h1>"

@route('/register')
def register():
    return "<h1>On the register Page</h1>"


@route('/article/<id>')
def article(id):
    return f"<h1> Article {id}</h1>"

@route('/posted', method='POST')
def posted():
    return '<h1> Posted </h1>'

if __name__ == '__main__':
    run(debug=True, reloader=True)