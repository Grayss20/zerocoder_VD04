from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def three_persons():
    context = {
        'caption': '3 persons',
        'city': 'Новосибирск'
    }
    return render_template('index.html', **context)


@app.route('/shablon/')
def three_persons_2():
    context = {
        'caption': '3 человека',
        'city': 'FGDAFYERYyj'
    }
    return render_template('index.html', **context)


@app.route('/ocuppations/')
def ocuppations():
    return render_template('main.html')


if __name__ == '__main__':
    app.run()
