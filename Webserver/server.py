from flask import Flask, render_template, url_for, request
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

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#      error = None
#      if request.method == 'POST':
#          if valid_login(request.form['username'],
#                         request.form['password']):
#              return log_the_user_in(request.form['username'])
#          else:
#              error = 'Invalid username/password'
#the code below is executed if the request method
#was GET or the credentials were invalid
#     return render_template('login.html', error=error)