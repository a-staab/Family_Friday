from flask import Flask, request, render_template
from model import db, connect_to_db
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)


@app.route("/")
def show_main():
    """Return landing page."""

    return render_template("main.html")



connect_to_db(app)

if __name__ == "__main__":
    app.debug = False
    app.jinja_env.auto_reload = app.debug
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run(host="0.0.0.0")