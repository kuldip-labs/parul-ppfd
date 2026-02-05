from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-very-secret-key'  # Change this!

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Mock Database
users = {}


class User(UserMixin):
    def __init__(self, id):
        self.id = id


@login_manager.user_loader
def load_user(user_id):
    return User(user_id) if user_id in users else None


@app.route('/')
def home():
    return f'<h1>Home</h1> <p>Hello, {current_user.id if current_user.is_authenticated else "Guest"}!</p>'


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users:
            flash('Username already exists!')
        else:
            # Hash the password for security
            users[username] = {'password': generate_password_hash(password)}
            flash('Registration successful! Please login.')
            return redirect(url_for('login'))
    return '''
        <form method="post">
            Username: <input type="text" name="username" required><br>
            Password: <input type="password" name="password" required><br>
            <button type="submit">Register</button>
        </form>
    '''


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user_data = users.get(username)
        if user_data and check_password_hash(user_data['password'], password):
            user = User(username)
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid username or password')
    return '''
        <form method="post">
            Username: <input type="text" name="username" required><br>
            Password: <input type="password" name="password" required><br>
            <button type="submit">Login</button>
        </form>
    '''


@app.route('/dashboard')
@login_required
def dashboard():
    return f'<h1>Welcome to your Dashboard, {current_user.id}!</h1><a href="/logout">Logout</a>'


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)