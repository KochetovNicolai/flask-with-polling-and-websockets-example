# see: http://flask.pocoo.org/docs/1.0/patterns/jquery/

from flask import Flask, jsonify, render_template, request
import io
import sys


app = Flask(__name__)


@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


@app.route('/_exec')
def exec_code():
    code = request.args.get('code')
    print(code)

    try:
        temp_buffer = io.StringIO()
        sys.stdout = temp_buffer
        exec(code)
        sys.stdout = sys.__stdout__
        res = temp_buffer.getvalue()
    except BaseException as e:
        res = str(e)

    return jsonify(result=res)


@app.route('/')
def index():
    return render_template('long_polling.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
