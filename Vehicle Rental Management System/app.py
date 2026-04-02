from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import os

# --- 1. APP CONFIGURATION ---
# We use the default Flask setup because your files are in the 'templates' folder.
app = Flask(__name__)
app.secret_key = "vrms_secure_key_2026"

# --- 2. DATABASE CONFIGURATION ---
# This ensures the database 'vrms.db' is created in the correct project folder.
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'vrms.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- 3. DATABASE MODEL (USER TABLE) ---
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# This command creates the database file automatically
with app.app_context():
    db.create_all()

# --- 4. THE ROUTES (PAGE CONNECTIONS) ---

@app.route('/')
def index():
    """Connects to templates/index.html"""
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Connects to templates/login.html"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Admin Bypass Check
        if email == "admin@gmail.com" and password == "123":
            session['user'] = "Admin"
            return redirect(url_for('admin_dashboard'))

        # Standard User Check
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            session['user'] = user.first_name
            return redirect(url_for('index'))
        else:
            flash("Invalid email or password!")
            
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Connects to templates/Register.html (Matching your Capital R)"""
    if request.method == 'POST':
        fname = request.form.get('first_name')
        lname = request.form.get('last_name')
        u_email = request.form.get('email')
        u_pwd = request.form.get('password')
        
        # Save new user to the database
        new_user = User(first_name=fname, last_name=lname, email=u_email, password=u_pwd)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
        
    return render_template('Register.html')

@app.route('/vehicles')
def vehicles():
    """Connects to templates/vehicle.html"""
    return render_template('vehicle.html')

@app.route('/admin-dashboard')
def admin_dashboard():
    """Connects to templates/admin-dashboard.html"""
    return render_template('admin-dashboard.html')

@app.route('/logout')
def logout():
    """Clears the session and goes home"""
    session.clear()
    return redirect(url_for('index'))

# --- 5. RUN THE SERVER ---
if __name__ == '__main__':
    app.run(debug=True)