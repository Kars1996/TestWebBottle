from bottle import route, run, error, request, response

@error(404)
def error404(error):
    return f'''
    <h1>The requested page</h1>
    <h2><b>{error}</b></h2>
    <h1> cannot be found on our servers</h1>
    '''

@error(405)
def error405(error):
    return '<h1> This method is not allowed</h1>'

@error(500)
def error500(error):
    return '<h1> Something went wrong on our end</h1>'

@route('/')
def index():
    if request.get_cookie("visited"):
        return "Welcome back! Nice to see you again"
    else:
        response.set_cookie("visited", "yes")
        return "Hello there! Nice to meet you"

@route('/0')
def zero():
    return 1 / 0

@route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"



run(debug=False, reloader=True, port=3001)
