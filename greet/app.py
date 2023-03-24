from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    """display the home page"""
    html = """
    <html>
      <body>
        <h1>Home Page</h1>
        <p>This is my first Flask app</p>
        <a href='/welcome'>Welcome Page</a>
        <a href='/welcome/home'>Welcome Home Page</a>
        <a href='/welcome/back'>Welcome Back Page</a>
      </body>
    </html>
    """
    return html

@app.route('/welcome')
def show_welcome():
    """ display the welcome page"""
    html = """
    <html>
      <body>
        <h1>Welcome Page</h1>
      </body>
    </html>
    """
    return html

@app.route('/welcome/home')
def show_welcome_home():
    """display welcome home page"""
    html = """
    <html>
      <body>
        <h1>Welcome Home Page</h1>
      </body>
    </html>
    """
    return html

@app.route('/welcome/back')
def show_welcome_back():
    """display welcome back page"""
    html = """
    <html>
      <body>
        <h1>Welcome Back Page</h1>
      </body>
    </html>
    """
    return html

