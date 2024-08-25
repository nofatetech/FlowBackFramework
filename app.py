from flows import app
from data import db

if __name__ == '__main__':
    with app.app_context():
        # Create the database and tables if they don't exist
        db.create_all()

    # Run the Flask application
    app.run(debug=True)
