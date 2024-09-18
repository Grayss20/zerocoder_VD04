from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def three_persons():
    return render_template('index.html')

@app.route('/ocuppations/')
def ocuppations():
    return render_template('main.html')

if __name__ == '__main__':
    app.run()