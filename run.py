import os
from taskmanager import app, db

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # this code creates the database schema without using console commands (from taskmanager import db)
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG") == 'True'
    )