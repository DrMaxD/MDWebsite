import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

database_url = os.getenv('DATABASE_URL')
if not database_url:
    raise RuntimeError("DATABASE_URL environment variable not set")

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

try:
    from db.schema.table import Table
except ImportError as e:
    raise ImportError(f"Error importing Table model: {e}")

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
        try:
            name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            contact_method = request.form.get('contact-method')
            message = request.form.get('message')

            new_entry = Table(
                name=name,
                email=email,
                phone=phone,
                contact_method=contact_method,
                message=message
            )

            db.session.add(new_entry)
            db.session.commit()

            return redirect(url_for('thank_you'))
        except Exception as e:
            return f"An error occurred while processing your request: {e}", 500

    return render_template('contactme.html')

@app.route('/thank_you')
def thank_you():
    return render_template('thankyou.html')

@app.route('/socials')
def socials():
    return render_template("socials.html")

if __name__ == "__main__":
    try:
        with app.app_context():
            db.create_all()
            print("Database tables created successfully.")
    except Exception as e:
        print(f"Error initializing database: {e}")

    app.run(debug=True)
