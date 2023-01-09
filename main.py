from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/achievements')
def achievements():
    return render_template('achievements.html')

@app.route('/support')
def support():
    return render_template('support.html')

if __name__ == '__main__':
    app.run(debug=True)