from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Employee(db.Model):
    """An employee."""

    __tablename__ = "employees"

    staff_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Unicode(30), nullable=False)
    last_name = db.Column(db.Unicode(30), nullable=False)


def connect_to_db(app, db_uri='postgresql:///staff_directory'):
    """Connect to the database."""

    # Making the database a default value for the db_uri parameter allows us to
    # pass in a different database for testing
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print "Connected to database"
