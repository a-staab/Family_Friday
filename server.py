from flask import Flask, request, render_template, redirect
from model import db, connect_to_db
from flask_debugtoolbar import DebugToolbarExtension
from model import Employee
import random
import json
import os

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]


@app.route("/")
def show_main():
    """Return landing page."""

    return render_template("main.html")


@app.route("/", methods=["POST"])
def add_teammate_to_db():

    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    action = request.form.get("action")

    if action == 'add':
        new_teammate = Employee(first_name=first_name,
                                last_name=last_name)
        db.session.add(new_teammate)

    elif action == 'disable':
        teammate_to_disable = Employee.query.filter(
            Employee.first_name == first_name,
            Employee.last_name == last_name).one()
        teammate_to_disable.is_active = False

    elif action == 'reactivate':
        teammate_to_reactivate = Employee.query.filter(
            Employee.first_name == first_name,
            Employee.last_name == last_name).one()
        teammate_to_reactivate.is_active = True

    db.session.commit()

    return redirect("/")


@app.route("/get_tables", methods=["GET"])
def display_groups():
    """Route for AJAX request. Pushes table assignments to the view."""

    tables = get_all_tables()
    view_tables = []

    for i in range(len(tables)):
        view_tables.append(
            ['%s %s' % (x.first_name, x.last_name) for x in tables[i]])

    return json.dumps(view_tables)


def get_table_assignments(teammates, results=None):
    """Given a list of teammates, returns a list of tuples of type
    (teammates per table, number of tables) such that the sum of the
    products of the number of tables and teammates per table for all of the
    tuples is equal to the total number of teammates."""

    if results is None:
        results = []

    if len(teammates) < 6:
        results.append(teammates)

    else:
        midpoint = len(teammates)/2
        get_table_assignments(teammates[:midpoint], results)
        get_table_assignments(teammates[midpoint:], results)
        return results


def randomize(assortment):
    """Given a list, randomly reorders its elements."""

    random.shuffle(assortment)


def get_all_tables():
    """Returns all staff, divided into groups of three, four, and/or five
    people each."""

    teammates = Employee.query.filter(Employee.is_active == 'True').all()
    randomize(teammates)

    return get_table_assignments(teammates)


connect_to_db(app)

if __name__ == "__main__":
    app.debug = False
    app.jinja_env.auto_reload = app.debug
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run(host="0.0.0.0")
