from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task

@app.route("/")
def home():
    """
    returns the task.html from templates
    """
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    """
    returns the categories.html from templates
    """
    return render_template("categories.html")


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    When the user clicks to add a new category it should render the template
    that contains a form, by displaying the form to users we are using the
    GET method to get the page. When the user submits the form it uses POST method
    """
    return render_template("add_category.html")
