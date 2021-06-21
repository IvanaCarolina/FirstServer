from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def homescreen():
    return render_template('index.html')

# @app.route('/<username>/<int:post_id>')
# def user(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/project.html')
def project():
    return render_template('project.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/components.html')
def components():
    return render_template('components.html')