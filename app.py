import sqlite3
import json
from flask import Flask, render_template, request, session, redirect
from helpers import hash_password, verify_password

app = Flask(__name__)

with open("./static/config.json") as file:
    config = json.load(file)

app.secret_key = config.get("secret_key")

connection = sqlite3.connect("./static/users.db", check_same_thread=False)
db = connection.cursor()

db.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, activity TEXT NOT NULL, username TEXT NOT NULL, FOREIGN KEY (username) REFERENCES users (username))")
db.execute("CREATE INDEX IF NOT EXISTS index_username ON items (username)")

@app.route("/")
def index():
    if "username" not in session:
        return render_template("login.html")
    
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return render_template("login.html", error="Username and Password fields cannot be empty.")
        
        try:
            result = db.execute("SELECT password FROM users WHERE username = ?", (username,)).fetchone()

            if result:
                hashed_password = result[0]
            else:
                return render_template("login.html", error="Username does not exist.")

            if not verify_password(password, hashed_password):
                return render_template("login.html", error="Password is incorrect.")
            
            session["username"] = username
        except:
            return render_template("login.html", error="An error occurred, try again.")
        
        return redirect("/")
    
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username or not password or not confirmation:
            return render_template("register.html", error="Username and Password fields cannot be empty.")

        if password != confirmation:
            return render_template("register.html", error="Password must match its confirmation.")
        
        try:
            db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hash_password(password)))
            session["username"] = username
        except:
            return render_template("register.html", error="An error occurred, try again.")

        return redirect("/")
    
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")