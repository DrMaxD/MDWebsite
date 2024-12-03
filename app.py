import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv  # Import the dotenv module to load environment variables

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Load database configuration from environment variables
db_name = os.getenv('db_name')
db_owner = os.getenv('db_owner')
db_pass = os.getenv('db_pass')

# Configure the app for PostgreSQL using the environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_owner}:{db_pass}@localhost:5432/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable SQLAlchemy event system for performance

# Initialize SQLAlchemy with the app
db = SQLAlchemy(app)

# Import the Table model (make sure to adjust this import based on where the Table model is located)
from db.schema.table import Table  # Ensure you have this path correct based on your project structure

# Define routes
@app.route('/')
def index():
    return render_template("index.html", root=True)

@app.route('/resume')
def resume():
    return render_template("resume.html")

@app.route('/aboutme')
def aboutme():
    return render_template("aboutme.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/contactme', methods=['GET', 'POST'])
def contactme():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        contact_method = request.form.get('contact-method')
        message = request.form.get('message')

        # Create a new record
        new_entry = Table(
            name=name,
            email=email,
            phone=phone,
            contact_method=contact_method,
            message=message
        )

        # Add the record to the database
        db.session.add(new_entry)
        db.session.commit()

        return redirect(url_for('thank_you'))

    return render_template('contactme.html')

@app.route('/thank_you')
def thank_you():
    return render_template('thankyou.html')

@app.route('/socials')
def socials():
    return render_template("socials.html")

if __name__ == "__main__":
    # Create the database tables
    with app.app_context():
        db.create_all()  # Ensure tables are created if they don't already exist
    app.run(debug=True)
