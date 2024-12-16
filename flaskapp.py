
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

# Insecure database simulation
users = {"admin": "password"}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return "Welcome, admin!"
        return "Invalid credentials."
    return render_template('login.html')

@app.route('/comment', methods=['GET', 'POST'])
def comment():
    if request.method == 'POST':
        comment = request.form['comment']
        return f"Comment submitted: {comment}"  # Vulnerable to XSS
    return render_template('comment.html')

if __name__ == '__main__':
    app.run(debug=True)
