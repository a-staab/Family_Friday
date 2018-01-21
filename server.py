from flask import Flask, request, render_template
from model import db, connect_to_db
from flask_debugtoolbar import DebugToolbarExtension
from random import choice
from model import Employee
import os

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]


@app.route("/")
def show_main():
    """Return landing page."""




    return render_template("main.html")


def get_table_sizes(teammates):
    """Given a list of teammates, returns a list of tuples of type
    (teammates per table, number of tables) such that the sum of the
    products of the number of tables and teammates per table for all of the
    tuples is equal to the total number of teammates."""

    if len(teammates) % 5 == 0:
        return [(5, (len(teammates) / 5))]

    # Checking if the teammates are evenly divisible by 4 and 3 helps
    # ensure some variety in the size of groups (assuming they're growing
    # relatively steadily). Otherwise, most people would dine in a group of
    # five most of the time.
    elif len(teammates) % 4 == 0:
        return [(4, (len(teammates) / 4))]

    elif len(teammates) % 3 == 0:
        return [(3, (len(teammates) / 3))]

    else:
        remainder = len(teammates) % 5
        if remainder == 1:
            return [(5, (len(teammates) / 5 - 1)), (3, 2)]
        elif remainder == 2:
            return [(5, (len(teammates) / 5 - 1)), (4, 1), (3, 1)]
        elif remainder == 3:
            return [(5, len(teammates) / 5), (3, 1)]
        elif remainder == 4:
            return [(5, len(teammates) / 5), (4, 1)]

    # TODO: Possibly write recursively?


def make_tables(num_assignees, num_tables, remaining_teammates, all_tables):
    """Given a list of teammates, assigns the given number of tables the given
    number of teammates and returns any unassigned teammates."""

    tables = []
    for i in range(num_tables):
        tables.append([])
        for j in range(num_assignees):
            tables[i].append(remaining_teammates.pop())

    all_tables.extend(tables)

    return remaining_teammates


def get_all_tables():
    """Returns all staff, divided into groups of three, four, and/or five
    people each."""

    all_tables = []
    teammates = Employee.query.all()

    for num_assignees, num_tables in get_table_sizes(teammates):
        teammates = make_tables(num_assignees, num_tables, teammates, all_tables)

    return all_tables


connect_to_db(app)

if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run(host="0.0.0.0")