from app import app
from app.forms import RegisterForm, BookForm
from flask import render_template, request, redirect, url_for



@app.get("/register")
def register():
    form = RegisterForm()
    return render_template("register.html", form=form)

@app.post("/register")
def register_post():
    return redirect(url_for("homepage"))

@app.route("/homepage")
def homepage():
    return render_template("home.html")

@app.get("/create_book")
def create_book():
    form = BookForm()
    return render_template("create_book.html", form=form)

@app.post("/create_book")
def create_book_post():
    return redirect(url_for("homepage"))