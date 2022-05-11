"""
importing required libraries and modules
"""
from flask import render_template, request, redirect, url_for
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
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    When the user clicks add category button - form template is rendered.
    When displaying the form we're using the GET method to get the page.
    When the user submits the form it uses POST method
    """
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")

# Look into defensive programming and error handling


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """
    edit category function
    """
    return render_template("edit_category.html")
