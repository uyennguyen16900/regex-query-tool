from flask import Flask, render_template, request
from regexQuery import *
from jinja2 import Environment, FileSystemLoader
# import os

app = Flask(__name__)

# PATH = os.path.dirname(os.path.abspath(__file__))
# TEMPLATE_ENVIRONMENT = Environment(
#     autoescape=True,
#     loader=FileSystemLoader(os.path.join(PATH, 'templates')),
#     trim_blocks=False)

@app.route('/')
def index():
    """Show homepage"""
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    """"""
    regex = request.form['regex']
    test_str = request.form['test_str']
    matches, indices = regex_query(regex, test_str)
    return render_template('result.html', regex=regex, matches=matches, indices=indices, test_str=test_str)
    # return TEMPLATE_ENVIRONMENT.get_template('result.html').render(matches=matches, indices=indices, test_str=test_str)

if __name__ == '__main__':
    app.run(debug=True)
