import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Check if the env.py file exists and import it if it does
if os.path.exists("env.py"):
    import env  # Ensure env.py sets environment variables using os.environ

# Initialize the Flask application
app = Flask(__name__)

# Set configuration variables from environment variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Import routes after initializing the app and db to avoid circular imports
from taskmanager import routes