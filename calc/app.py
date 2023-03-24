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
        </body>
      </html>
    """
    return html

@app.route('/math/<operation>')
def calculate_result(operation):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = OPERATIONS[operation](a, b)
    return str(result)

OPERATIONS = {
    'add': add,
    'subtract': sub,
    'multiply': mult,
    'divide': div
}

# @app.route('/add')
# def display_add():
#     print(request.args) # ImmutableMultiDict([('a', '1'), ('b', '2')])
#     a = int(request.args['a'])
#     b = int(request.args['b'])
#     sum = add(a,b)
#     return f"<p>The sum of {a} and {b} is: {sum}</p>"

# @app.route('/subtract')
# def display_subtract():
#     a = int(request.args['a'])
#     b = int(request.args['b'])
#     remainder = sub(a, b)
#     return f"<p>The remainder of {a} minus {b} is: {remainder}</p>"

# @app.route('/multiply')
# def display_multiply():
#     a = int(request.args['a'])
#     b = int(request.args['b'])
#     product = mult(a, b)
#     return f"<p>The product of {a} and {b} is: {product}</p>"

# @app.route('/divide')
# def display_divide():
#     a = int(request.args['a'])
#     b = int(request.args['b'])
#     result = int(div(a, b))
#     return f"<p>{a} divided by {b} is: {result}</p>"

