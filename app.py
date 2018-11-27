from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

counts = 0


@app.route('/request-counter/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def request_counter():
    global counts
    counts += 1
    return redirect(url_for('index'))


@app.route('/statistics/')
def statistics():
    global counts
    return render_template('statistics.html', counts=counts)



@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
