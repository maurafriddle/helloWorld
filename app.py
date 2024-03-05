from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Maura Friddle! I am adding my first code change.'

@app.route('/about-css')
def about_css():  # put application's code here
    return render_template('about-css.html')

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
