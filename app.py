from flask import Flask, render_template, redirect

app = Flask(__name__)

counts = 0


@app.route('/request-counter/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def request_counter():
    global counts
    counts += 1
    print(counts)
    return str(counts)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
