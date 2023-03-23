from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/')
def home_page():
    """display home page"""
    html = """
      <html>
        <body>
          <h1>A Simple Calculator built with Flask</h1>
          <a href='/add'>Add</a>
          <a href='/subtract'>Subtract</a>
          <a href='/multiply'>Multiply</a>
          <a href='/divide'>Divide</a>
        </body>
      </html>
    """
    return html

@app.route('/add')
def display_add():
    print(request.args) # ImmutableMultiDict([('a', '1'), ('b', '2')])
    a = int(request.args['a'])
    b = int(request.args['b'])
    sum = add(a,b)
    return f"<p>The sum of {a} and {b} is: {sum}</p>"

@app.route('/subtract')
def display_subtract():
    a = int(request.args['a'])
    b = int(request.args['b'])
    remainder = sub(a, b)
    return f"<p>The remainder of {a} minus {b} is: {remainder}</p>"

@app.route('/multiply')
def display_multiply():
    a = int(request.args['a'])
    b = int(request.args['b'])
    product = mult(a, b)
    return f"<p>The product of {a} and {b} is: {product}</p>"

@app.route('/divide')
def display_divide():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = int(div(a, b))
    return f"<p>{a} divided by {b} is: {result}</p>"