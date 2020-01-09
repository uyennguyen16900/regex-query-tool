from flask import Flask, render_template, request
from regexQuery import *
from jinja2 import Environment, BaseLoader

app = Flask(__name__)

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
    return render_template('result.html', matches=matches, indices=indices, test_str=test_str)

if __name__ == '__main__':
    app.run(debug=True)
