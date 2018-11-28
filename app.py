from flask import Flask, render_template, redirect, url_for, request
import csv

app = Flask(__name__)


@app.route('/request-counter/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def request_counter():
    counts = load_counts()
    counts[request.method] += 1
    save_counts(counts)
    return redirect(url_for('index'))


@app.route('/statistics/')
def statistics():
    counts = load_counts()
    return render_template('statistics.html', counts=counts)



@app.route('/')
def index():
    return render_template('index.html')


def load_counts():
    counts = {}
    with open("counts.txt") as f:
        csv_reader = csv.reader(f, delimiter=':')
        for row in csv_reader:
            counts[row[0]] = int(row[1])
    return counts


def save_counts(counts):
    print("counts")
    print(counts)
    with open("counts.txt", "w") as f:
        csv_writer = csv.writer(f, delimiter=':')
        for row in counts:
            csv_writer.writerow([row, counts[row]])
    return 1


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
