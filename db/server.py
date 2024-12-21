import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv  # For loading environment variables

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

# Initialize the SQLAlchemy instance
db = SQLAlchemy(app)

# Import routes and models (after initializing db)
from db.schema.table import contactme  # Make sure the path is correct

# Create all the tables from the models (assuming Table uses db)
with app.app_context():
    db.create_all()  # Creates all tables if they don't exist already

if __name__ == "__main__":
    # Run the Flask app in debug mode
    app.run(debug=True)