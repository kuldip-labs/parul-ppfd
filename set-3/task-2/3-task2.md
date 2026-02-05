## Building a full-scale authentication system from scratch 
* Flask is the go-to framework. It’s lightweight and easy to understand.
* To get this running, we'll use Flask-Login for session management and Werkzeug for secure password hashing (never store passwords as plain text!).
#### Prerequisites
You'll need to install Flask and its login extension:
`pip install flask flask-login`

#### The Application Code (app.py)
* This script handles the routing, the "database" (a simple dictionary for this example), and the login logic.


|Component| Purpose |
|---|--------------|
| UserMixin	| Provides default implementations for properties like is_authenticated.|
| generate_password_hash| Turns "Password123" into a scrambled string that can't be easily reversed.|
|@login_required| A decorator that protects specific routes from being accessed by unlogged users. |
| SECRET_KEY | 	Used to sign session cookies so users can't forge their identity. |