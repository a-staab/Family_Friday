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


def example_data():
    """Sample data for testing."""

    # Tests using instantiation
    jack = Employee(first_name="Jack", last_name="Toler")
    paul = Employee(first_name="Paul", last_name="Johnson")
    anna = Employee(first_name="Anna", last_name="Whitley")
    ethan = Employee(first_name="Ethan", last_name="Pratt")
    latoya = Employee(first_name="Latoya", last_name="Erickson")
    janalynn = Employee(first_name="Janalynn", last_name="Headly")
    scott = Employee(first_name="Scott", last_name="Davis")
    jamal = Employee(first_name="Jamal", last_name="Curwood")
    evelyn = Employee(first_name="Evelyn", last_name="Howe")
    mariah = Employee(first_name="Mariah", last_name="Dawson")
    jamie = Employee(first_name="Jamie", last_name="Finch")

    db.session.add_all([jack, paul, anna, ethan, latoya, janalynn, scott, jamal,
                        evelyn, mariah, jamie])

    db.session.commit()


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print "Connected to database"
